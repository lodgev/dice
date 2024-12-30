import csv
import os
from .abstract_highscore import AbstractHighScore

class HighScoreSr(AbstractHighScore):
    def __init__(self, file_path="./DicePersist/db/highscores.csv"):
        self.file_path = file_path

    def add_score(self, player_name, score, date_obtained, strategy_type):
        """Додає запис у CSV."""
        with open(self.file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([player_name, score, date_obtained, strategy_type])

    def get_top_scores(self, limit=10):
        """Повертає топ-результати."""
        try:
            with open(self.file_path, mode="r", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)  # Пропускаємо заголовки (перший рядок)
                scores = sorted(
                    reader,
                    key=lambda x: int(x[1]),  # Перетворюємо другий елемент на число
                    reverse=True
                )
                return scores[:limit]
        except FileNotFoundError:
            return []
        except ValueError as e:
            print(f"Error reading scores: {e}")
            return []
