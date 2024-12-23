class HighScore:
    def __init__(self):
        self.scores = []

    def add_score(self, name, score):
        """Додає новий запис до таблиці рекордів."""
        self.scores.append({"name": name, "score": score})
        self.scores = sorted(self.scores, key=lambda x: x["score"], reverse=True)

    def get_top_scores(self, limit=10):
        """Повертає топ-результати."""
        return self.scores[:limit]
