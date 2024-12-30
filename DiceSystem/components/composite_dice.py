from .dice_component import DiceComponent

class CompositeDice(DiceComponent):
    """Composite для об'єднання декількох кубиків."""

    def __init__(self):
        self.children = []

    def add(self, dice):
        """Додає кубик до Composite."""
        self.children.append(dice)

    def remove(self, dice):
        """Видаляє кубик із Composite."""
        self.children.remove(dice)

    def roll(self):
        """Симулює кидок усіх кубиків у Composite."""
        return [child.roll() for child in self.children]
