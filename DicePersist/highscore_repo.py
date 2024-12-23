from pymongo import MongoClient
import logging

logging.basicConfig(level=logging.INFO)

class HighScoreRepo:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="dice_game", collection_name="highscores"):
        """Ініціалізація підключення до бази даних."""
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
    
    def add_score(self, player_name, score, date_obtained):
        """Додає запис про результат гри з датою."""
        record = {
            "player_name": player_name,
            "score": score,
            "date_obtained": date_obtained
        }
        self.collection.insert_one(record)


    def get_top_scores(self, limit=10):
        return list(self.collection.find().sort("score", -1).limit(limit))

    def clear_scores(self):
        """Очищує всі записи (для тестування)."""
        self.collection.delete_many({})
