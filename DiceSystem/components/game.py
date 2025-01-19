from .composite_dice import CompositeDice
from .scoring_strategy import StandardScoring
from .single_dice import SingleDice 

class GameObserver:
    def update(self, game_state):
        pass

class Game:
    def __init__(self, player_name, nrounds=10, scoring_strategy=None):
        self.player_name = player_name
        self.nrounds = nrounds
        self.current_round = 0
        self.total_score = 0
        self.observers = []  
        self.scoring_strategy = scoring_strategy or StandardScoring() 

    
        self.dice = CompositeDice()
        self.dice.add(SingleDice())
        self.dice.add(SingleDice())

    def roll_dices(self):
        if self.current_round >= self.nrounds:
            raise ValueError("Game is over. No more rounds left.")

        self.current_round += 1
        rolls = self.dice.roll()
        round_score = self.scoring_strategy.calculate_score(rolls, sum(rolls), self.current_round)
        self.total_score += round_score

        self.notify_observers()  
        return rolls, round_score, self.current_round

    def is_game_over(self):
        return self.current_round >= self.nrounds



    def add_observer(self, observer: GameObserver):

        self.observers.append(observer)

    def notify_observers(self):

        game_state = {
            "player_name": self.player_name,
            "current_round": self.current_round,
            "total_score": self.total_score,
            "is_game_over": self.is_game_over(),
        }
        for observer in self.observers:
            observer.update(game_state)

