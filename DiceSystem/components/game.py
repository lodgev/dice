from .composite_dice import CompositeDice
from .single_dice import SingleDice
from .scoring_strategy import StandardScoring  # Підключаємо стандартну стратегію

class Game:
    def __init__(self, player_name, nrounds=10, scoring_strategy=None):
        self.player_name = player_name
        self.nrounds = nrounds
        self.current_round = 0
        self.total_score = 0
        # використання Design Pattern - Strategy
        self.scoring_strategy = scoring_strategy or StandardScoring()  # За замовчуванням StandardScoring

        # використання Design Pattern - Composite
        # CompositeDice: об'єднання двох кубиків
        self.dice = CompositeDice()
        self.dice.add(SingleDice())
        self.dice.add(SingleDice())

    def roll_dices(self):
        """Симулює кидки кубиків і обчислює рахунок раунду."""
        if self.current_round >= self.nrounds:
            raise ValueError("Game is over. No more rounds left.")

        self.current_round += 1
        rolls = self.dice.roll()
        round_score = self.scoring_strategy.calculate_score(rolls, sum(rolls), self.current_round)
        self.total_score += round_score
        return rolls, round_score, self.current_round

    def is_game_over(self):
        """Перевіряє, чи гра завершена."""
        return self.current_round >= self.nrounds
