# from .dice_component import DiceComponent
from .dice_component import DiceComponent


class CompositeDice(DiceComponent):
    """Composite для об'єднання декількох кубиків."""

    def __init__(self):
        self.children = []
        self.observers = []  # List of registered observers


    def add(self, dice):
        """Додає кубик до Composite."""
        self.children.append(dice)

    def remove(self, dice):
        """Видаляє кубик із Composite."""
        self.children.remove(dice)

    def roll(self):
        """Симулює кидок усіх кубиків у Composite."""
        # return [child.roll() for child in self.children]
        rolls = [child.roll() for child in self.children]
        self.notify_observers(rolls)  # Notify observers of the roll results
        return rolls

    def add_observer(self, observer):
        """Registers an observer."""
        self.observers.append(observer)

    def remove_observer(self, observer):
        """Removes an observer."""
        self.observers.remove(observer)

    def notify_observers(self, roll_results):
        """Notifies all registered observers with the dice roll results."""
        for observer in self.observers:
            observer.update(roll_results)

    def __iter__(self):
        """Повертає ітератор"""
        return DiceIterator(self.children)


class DiceIterator:
    """Iterator for iterating over dice in CompositeDice."""
    def __init__(self, dice_list):
        self._dice_list = dice_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._dice_list):
            dice = self._dice_list[self._index]
            self._index += 1
            return dice
        else:
            raise StopIteration


class DiceObserver:
    """Interface for dice observers that listen to dice roll events."""
    def update(self, roll_results):
        """This method is called when dice are rolled."""
        pass


