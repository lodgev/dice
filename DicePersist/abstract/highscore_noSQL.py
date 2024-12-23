from pymongo import MongoClient
from .abstract_highscore import AbstractHighScore

class HighScoreNoSQL(AbstractHighScore):
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="dice_game", collection_name="highscores"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add_score(self, player_name, score, date_obtained):
        record = {"player_name": player_name, "score": score, "date_obtained": date_obtained}
        self.collection.insert_one(record)

    def get_top_scores(self, limit=10):
        return list(self.collection.find().sort("score", -1).limit(limit))
