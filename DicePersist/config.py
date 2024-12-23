class Config:
    """Конфігурація бази даних."""
    MONGO_URI = "mongodb://localhost:27017/"
    DATABASE_NAME = "dice_game"
    HIGHSCORE_COLLECTION = "high_scores"
