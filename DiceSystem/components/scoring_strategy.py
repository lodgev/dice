class ScoringStrategy:
    """Інтерфейс для стратегій підрахунку очок."""
    def calculate_score(self, rolls, round_score, current_round):
        raise NotImplementedError("Subclasses must implement this method")


class StandardScoring(ScoringStrategy):
    """Стандартна стратегія: +10, якщо сума кубиків дорівнює 7."""
    def calculate_score(self, rolls, round_score, current_round):
        print("Using StandardScoring")
        if sum(rolls) == 7:
            return 10
        return 0


class SumScoring(ScoringStrategy):
    """Сумування очок: додає суму значень кубиків до загального рахунку."""
    def calculate_score(self, rolls, round_score, current_round):
        print("Using SumScoring")
        return round_score


class DoubleScoring(ScoringStrategy):
    """Подвоєння очок: подвоює результат, якщо випадає 6."""
    def calculate_score(self, rolls, round_score, current_round):
        print("Using DoubleScoring")
        if 6 in rolls:
            return round_score * 2
        return round_score
