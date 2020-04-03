import abc
from typing import Type


class FlyBehavior(abc.ABC):
    @abc.abstractmethod
    def fly(self) -> None:
        pass


class QuackBehavior(abc.ABC):
    @abc.abstractmethod
    def quack(self) -> None:
        pass


class Duck(abc.ABC):
    @property
    @abc.abstractmethod
    def fly_behavior(self) -> FlyBehavior:
        pass

    @property
    @abc.abstractmethod
    def quack_behavior(self) -> QuackBehavior:
        pass

    @fly_behavior.setter  # pragma: no cover
    def fly_behavior(self, fb: Type[FlyBehavior]) -> None:
        self.fly_behavior = fb()

    @quack_behavior.setter  # pragma: no cover
    def quack_behavior(self, qb: Type[QuackBehavior]) -> None:
        self.quack_behavior = qb()

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
