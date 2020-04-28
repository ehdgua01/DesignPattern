"""
Simulation of adapter pattern

>>> from .models import MallardDuck, WildTurkey
>>> duck = MallardDuck()
>>> turkey = WildTurkey()
>>> turkey_adapter = TurkeyAdapter(turkey)
>>> turkey.gobble()
칠면조: 골골
>>> turkey.fly()
칠면조: 나는 중(단거리)
>>> duck.quack()
물오리: 꽥
>>> duck.fly()
물오리: 나는 중(장거리)
>>> turkey_adapter.fly()
칠면조: 나는 중(단거리)
>>> turkey_adapter.quack()
칠면조: 골골
"""
from .interfaces import Duck
from .models import Turkey


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        self.turkey.fly()
