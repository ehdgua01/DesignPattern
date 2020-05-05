from .interfaces import Quackable


class MallardDuck(Quackable):
    def quack(self) -> None:
        print("꽥")


class RedheadDuck(Quackable):
    def quack(self) -> None:
        print("꽥")


class DuckCall(Quackable):
    def quack(self) -> None:
        print("꽈악")


class RubberDuck(Quackable):
    def quack(self) -> None:
        print("Squeak")
