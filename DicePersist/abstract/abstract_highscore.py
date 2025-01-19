from abc import ABC, abstractmethod

class AbstractHighScore(ABC):
    @abstractmethod
    def add_score(self, player_name, score,  date_obtained, strategy_type):
        pass

    @abstractmethod
    def get_top_scores(self, limit=10):
        pass

