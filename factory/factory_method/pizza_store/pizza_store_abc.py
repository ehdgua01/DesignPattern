import abc
import enum
from typing import TypeVar, List


PIZZA = TypeVar("PIZZA", bound="Pizza")


class Pizza(abc.ABC):
    @property
    @abc.abstractmethod
    def toppings(self) -> List[str]:
        pass

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def sauce(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def dough(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def cooking_time(self) -> int:
        pass

    def prepare(self) -> None:
        print(
            f"[{self.name}] "
            f"반죽: {self.dough}, "
            f"소스: {self.sauce}, "
            f'토핑: {", ".join(self.toppings)}'
        )

    def bake(self) -> None:
        print(f"[{self.name}] 조리 시간: {self.cooking_time} 분")

    def cut(self) -> None:
        print(f"[{self.name}] 자름")

    def box(self) -> None:
        print(f"[{self.name}] 상자에 담음")


class PizzaFactory(abc.ABC):
    def order(self, pizza_type: enum.Enum) -> None:
        __pizza: PIZZA = self.create_pizza(pizza_type)
        __pizza.prepare()
        __pizza.bake()
        __pizza.cut()
        __pizza.box()

    @abc.abstractmethod
    def create_pizza(self, pizza_type: enum.Enum) -> PIZZA:
        pass
