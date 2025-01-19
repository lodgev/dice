import random
from .dice_component import DiceComponent

class SingleDice(DiceComponent):

    def roll(self):
        return random.randint(1, 6)
