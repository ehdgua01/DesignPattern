import abc
import enum
from .pizza_abc import PIZZA


class PizzaStore(abc.ABC):
    def order(self, pizza_type: enum.Enum) -> None:
        __pizza: PIZZA = self.create_pizza(pizza_type)
        __pizza.prepare()
        __pizza.bake()
        __pizza.cut()
        __pizza.box()

    @abc.abstractmethod
    def create_pizza(self, pizza_type: enum.Enum) -> PIZZA:
        pass
