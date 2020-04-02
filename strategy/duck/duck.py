"""
Simulation duck
>>> mallard = MallardDuck()
>>> mallard.display()
물오리
>>> mallard.perform_fly()
날 수 있음(날개)
>>> mallard.perform_quack()
꽥
>>> model = ModelDuck()
>>> model.display()
모형 오리
>>> model.perform_fly()
날 수 없음
>>> model.perform_quack()
꽥
>>> model.set_fly_behavior(FlyRocketPower)
>>> model.perform_fly()
날 수 있음(로켓)
>>> model.set_quack_behavior(MuteQuack)
>>> model.perform_quack()
조용
"""
import abc
from typing import Type


class FlyBehavior(abc.ABC):
    @abc.abstractmethod
    def fly(self) -> None:
        pass


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("날 수 있음(날개)")


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("날 수 없음")


class FlyRocketPower(FlyBehavior):
    def fly(self) -> None:
        print('날 수 있음(로켓)')


class QuackBehavior(abc.ABC):
    @abc.abstractmethod
    def quack(self) -> None:
        pass


class Quack(QuackBehavior):
    def quack(self) -> None:
        print("꽥")


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print("조용")


class Duck(abc.ABC):
    def __init__(self) -> None:
        self._fly_behavior = None
        self._quack_behavior = None

    @property
    @abc.abstractmethod
    def fly_behavior(self) -> FlyBehavior:
        return self._fly_behavior

    @property
    @abc.abstractmethod
    def quack_behavior(self) -> QuackBehavior:
        return self._quack_behavior

    @fly_behavior.setter  # pragma: no cover
    def fly_behavior(self, fb: Type[FlyBehavior]) -> None:
        self._fly_behavior = fb()

    @quack_behavior.setter  # pragma: no cover
    def quack_behavior(self, qb: Type[QuackBehavior]) -> None:
        self._quack_behavior = qb()

    @abc.abstractmethod
    def display(self) -> None:
        pass

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb: Type[FlyBehavior]) -> None:
        self.fly_behavior = fb()

    def set_quack_behavior(self, qb: Type[QuackBehavior]) -> None:
        self.quack_behavior = qb()


class MallardDuck(Duck):
    fly_behavior = FlyWithWings()
    quack_behavior = Quack()

    def display(self) -> None:
        print("물오리")


class ModelDuck(Duck):
    fly_behavior = FlyNoWay()
    quack_behavior = Quack()

    def display(self) -> None:
        print('모형 오리')
