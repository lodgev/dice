import sqlite3
from .abstract_highscore import AbstractHighScore

class HighScoreJDBC(AbstractHighScore):
    def __init__(self, db_path="./DicePersist/db/highscores.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)  # Додано check_same_thread=False
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS highscores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT,
                score INTEGER,
                date_obtained TEXT,
                strategy_type TEXT
            )
        """)
        self.conn.commit()
        
    def add_score(self, player_name, score, date_obtained, strategy_type):
        """Додає запис у SQL базу даних."""
        self.cursor.execute(
            "INSERT INTO highscores (player_name, score, date_obtained, strategy_type) VALUES (?, ?, ?, ?)",
            (player_name, score, date_obtained, strategy_type)
        )
        self.conn.commit()

    def get_top_scores(self, limit=10):
        """Повертає топ-результати."""
        self.cursor.execute(
            "SELECT player_name, score, date_obtained, strategy_type FROM highscores ORDER BY score DESC LIMIT ?",
            (limit,)
        )
        return self.cursor.fetchall()

    def close_connection(self):
        """Закриває з'єднання з базою даних."""
        self.cursor.close()
        self.conn.close()
