import csv
import os
from .abstract_highscore import AbstractHighScore

class HighScoreSr(AbstractHighScore):
    def __init__(self, file_path="./DicePersist/db/highscores.csv"):
        self.file_path = file_path

    def add_score(self, player_name, score, date_obtained):
        # Перевірка, чи файл існує
        file_exists = os.path.exists(self.file_path)

        with open(self.file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            
            # Якщо файл новий, записуємо заголовки
            if not file_exists:
                writer.writerow(["player_name", "score", "date_obtained"])
            
            # Записуємо дані
            writer.writerow([player_name, score, date_obtained])

    def get_top_scores(self, limit=10):
        try:
            with open(self.file_path, mode="r", newline="") as file:
                reader = csv.reader(file)
                # Пропускаємо заголовки
                next(reader, None)
                scores = sorted(reader, key=lambda x: int(x[1]), reverse=True)
                return scores[:limit]
        except FileNotFoundError:
            return []