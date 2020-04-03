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
from .duck_abc import FlyBehavior, QuackBehavior, Duck


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("날 수 있음(날개)")


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("날 수 없음")


class FlyRocketPower(FlyBehavior):
    def fly(self) -> None:
        print("날 수 있음(로켓)")


class Quack(QuackBehavior):
    def quack(self) -> None:
        print("꽥")


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print("조용")


class MallardDuck(Duck):
    fly_behavior = FlyWithWings()
    quack_behavior = Quack()

    def display(self) -> None:
        print("물오리")


class ModelDuck(Duck):
    fly_behavior = FlyNoWay()
    quack_behavior = Quack()

    def display(self) -> None:
        print("모형 오리")
