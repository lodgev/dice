import random
from .dice_component import DiceComponent

class SingleDice(DiceComponent):
    """Компонент для одиночного кубика."""

    def roll(self):
        """Симулює кидок одиночного кубика (1-6)."""
        return random.randint(1, 6)
