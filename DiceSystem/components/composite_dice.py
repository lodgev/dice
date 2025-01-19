from .dice_component import DiceComponent


class CompositeDice(DiceComponent):

    def __init__(self):
        self.children = []
        self.observers = []  


    def add(self, dice):
        self.children.append(dice)

    def remove(self, dice):
        self.children.remove(dice)

    def roll(self):
        rolls = [child.roll() for child in self.children]
        self.notify_observers(rolls) 
        return rolls

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, roll_results):
        for observer in self.observers:
            observer.update(roll_results)

    def __iter__(self):
        return DiceIterator(self.children)


class DiceIterator:
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
    def update(self, roll_results):
        pass


