class ScoringStrategy:
    def calculate_score(self, rolls, round_score, current_round):
        raise NotImplementedError("Subclasses must implement this method")


class StandardScoring(ScoringStrategy):
    def calculate_score(self, rolls, round_score, current_round):
        print("Using StandardScoring")
        if sum(rolls) == 7:
            return 10
        return 0


class SumScoring(ScoringStrategy):
    def calculate_score(self, rolls, round_score, current_round):
        print("Using SumScoring")
        return round_score


class DoubleScoring(ScoringStrategy):
    def calculate_score(self, rolls, round_score, current_round):
        print("Using DoubleScoring")
        if 6 in rolls:
            return round_score * 2
        return round_score
