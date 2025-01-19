import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.game import Game
from datetime import datetime

# Design Pattern:  Abstract Factory
from DicePersist.factory.persist_kit import PersistKit
from DicePersist.abstract.highscore_noSQL import HighScoreNoSQL
from DicePersist.abstract.highscore_JDBC import HighScoreJDBC
from DicePersist.abstract.highscore_sr import HighScoreSr

# Design Pattern: Composite
from DicePersist.composite.single_database import SingleDatabase
from DicePersist.composite.composite_score_manager import CompositeScoreManager

# Design Pattern: Strategy
from components.scoring_strategy import StandardScoring, SumScoring, DoubleScoring

# Design Pattern: Singleton
class SingletonMeta(type):
    """Мета-клас для реалізації Singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DiceSystem(metaclass=SingletonMeta):
    
    def __init__(self, persistence_type="nosql", scoring_strategy=None):
        self.game_instance = None
        # self.game_number = 0
        self.persistence_type = persistence_type
        self._initialize_repo()
        self.scoring_strategy = scoring_strategy or StandardScoring()
        
        # Composite Score Manager
        self.score_manager = CompositeScoreManager()
        self.score_manager.add("nosql", SingleDatabase(HighScoreNoSQL()))
        self.score_manager.add("jdbc", SingleDatabase(HighScoreJDBC()))
        self.score_manager.add("sr", SingleDatabase(HighScoreSr()))

        self.score_manager.set_active(self.persistence_type)
        
        print("Databases in CompositeScoreManager:")
        for persistence_type, component in self.score_manager.children.items():
            print(f"{persistence_type}: {component}")

    def _initialize_repo(self):
        factory = PersistKit.get_persistence_kit(self.persistence_type)
        self.highscore_repo = factory.create_highscore()
    

    def switch_persistence(self, new_persistence_type):
        if self.persistence_type != new_persistence_type:
            self.persistence_type = new_persistence_type
            self.score_manager.set_active(self.persistence_type)  

    def set_scoring_strategy(self, strategy_name):
            if strategy_name == "standard":
                self.scoring_strategy = StandardScoring()
            elif strategy_name == "sum":
                self.scoring_strategy = SumScoring()
            elif strategy_name == "double":
                self.scoring_strategy = DoubleScoring()
            else:
                raise ValueError(f"Unknown strategy: {strategy_name}")

            print(f"Scoring strategy set to: {strategy_name}")



    def start_game(self, player_name):
        self.game_instance = Game(player_name, scoring_strategy=self.scoring_strategy)
        return f"Game initialized! Let's start."


    def roll_dice(self):
        if not self.game_instance:
            raise ValueError("Game not initialized. Call start_game first.")
        if self.game_instance.is_game_over():
            self._save_score()
            return "Game over! No more rounds left."
        
        result = self.game_instance.roll_dices()
        if self.game_instance.is_game_over():
            self._save_score()
        return result

    
    def _save_score(self):
        final_score = self.game_instance.total_score
        date_obtained = datetime.now().strftime("%d.%m.%Y")
        strategy_type = self.scoring_strategy.__class__.__name__  

        self.score_manager.add_score(
            self.game_instance.player_name,
            final_score,
            date_obtained,
            strategy_type
        )



    def get_current_round(self):
        return self.game_instance.current_round if self.game_instance else 0

    def get_total_score(self):
        return self.game_instance.total_score if self.game_instance else 0
    
    def get_combined_top_scores(self, limit=10, strategy_type=None):
        scores = self.score_manager.get_scores() 

        if strategy_type:
            scores = [score for score in scores if score.get("strategy_type") == strategy_type]
            
        return sorted(scores, key=lambda x: x["score"], reverse=True)[:limit]

