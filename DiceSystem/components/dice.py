import random

class Dice:
    def __init__(self):
        self.value = 1

    def roll(self):
        """Викидає значення кубика від 1 до 6."""
        self.value = random.randint(1, 6)
        return self.value
