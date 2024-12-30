import random

class DiceComponent:
    """Базовий клас для компонентів кубиків."""

    def roll(self):
        """Симулює кидок кубика."""
        raise NotImplementedError("This method should be overridden in a subclass")
