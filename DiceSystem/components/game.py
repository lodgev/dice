from .dice import Dice
from .player import Player

class Game:
    def __init__(self, player_name, nrounds=10):
        self.player_name = player_name
        self.nrounds = nrounds
        self.current_round = 0
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.total_score = 0
    
    def roll_dices(self):
        roll1 = self.dice1.roll()
        roll2 = self.dice2.roll()
        self.current_round += 1  # Збільшуємо номер поточного раунду
        # print(f"Round: {self.current_round}/{self.nrounds}")
        round_score = self.calculate_score(roll1, roll2)
        self.total_score += round_score
        return roll1, roll2, round_score, self.current_round


    def calculate_score(self, roll1, roll2):
        """Розраховує очки за раунд."""
        return 10 if roll1 + roll2 == 7 else 0

    def is_game_over(self):
        """Перевіряє, чи гра завершена."""
        # print(self.current_round, " - ", self.nrounds)
        return self.current_round >= self.nrounds
