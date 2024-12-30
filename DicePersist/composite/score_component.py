class ScoreComponent:
    """Базовий клас для компонентів управління рахунками."""
    def add_score(self, player_name, score, date_obtained, strategy_type):
        raise NotImplementedError

    def get_scores(self):
        raise NotImplementedError