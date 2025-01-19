from .score_component import ScoreComponent

class SingleDatabase(ScoreComponent):
    """Компонент для роботи з однією базою даних."""

    def __init__(self, db_repo):
        self.db_repo = db_repo

    def add_score(self, player_name, score, date_obtained, strategy_type):
        """Додає рахунок у базу даних."""
        self.db_repo.add_score(player_name, score, date_obtained, strategy_type)

    def get_scores(self):
        """Отримує рахунки з бази даних."""
        return self.db_repo.get_top_scores()
