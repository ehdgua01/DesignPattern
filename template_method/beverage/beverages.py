"""
Simulation of template method pattern

>>> coffee = Coffee()
>>> tea = Tea()
>>> coffee.prepare_recipe()
물 끓이는 중
커피 우려내는 중
컵에 따르는 중
설탕과 커피를 추가하는 중
>>> tea.prepare_recipe()
물 끓이는 중
차 우려내는 중
컵에 따르는 중
레몬을 추가하는 중
"""
from .interfaces import CaffeineBeverage


class Coffee(CaffeineBeverage):
    def brew(self) -> None:
        print("커피 우려내는 중")

    def add_condiments(self) -> None:
        print("설탕과 커피를 추가하는 중")


class Tea(CaffeineBeverage):
    def brew(self) -> None:
        print("차 우려내는 중")

    def add_condiments(self) -> None:
        print("레몬을 추가하는 중")
