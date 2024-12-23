class Entry:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def to_dict(self):
        """Перетворює об'єкт Entry на словник."""
        return {"name": self.name, "score": self.score}

    @classmethod
    def from_dict(cls, data):
        """Створює об'єкт Entry із словника."""
        return cls(name=data["name"], score=data["score"])
