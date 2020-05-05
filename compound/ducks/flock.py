"""
Simulation of compound pattern(Strategy, Adapter, Composite)

>>> from .ducks import MallardDuck, RedheadDuck, DuckCall, RubberDuck
>>> from .geese import LandesGoose
>>> from .adapters import GooseAdapter
>>> flock = Flock()
>>> flock.add_quacker(MallardDuck())
>>> flock.add_quacker(RedheadDuck())
>>> flock.add_quacker(DuckCall())
>>> flock.add_quacker(RubberDuck())
>>> flock.add_quacker(GooseAdapter(LandesGoose()))
>>> flock.quack()
꽥
꽥
꽈악
Squeak
꽥
"""
from typing import List
from .interfaces import Quackable


class Flock(object):
    def __init__(self) -> None:
        self.quackers: List[Quackable] = []

    def add_quacker(self, quacker: Quackable):
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()
