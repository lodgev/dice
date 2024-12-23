class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, points):
        """Додає очки до рахунку гравця."""
        self.score += points

    def get_score(self):
        """Повертає поточний рахунок гравця."""
        return self.score
