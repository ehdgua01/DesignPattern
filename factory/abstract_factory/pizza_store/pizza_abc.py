import abc
from typing import TypeVar, Union

from .ingredient_abc import DOUGH, CHEESE, BULGOGI


PIZZA = TypeVar("PIZZA", bound="Pizza")


class Pizza(abc.ABC):
    def __init__(self) -> None:
        self.dough: Union[DOUGH, None] = None
        self.cheese: Union[CHEESE, None] = None
        self.bulgogi: Union[BULGOGI, None] = None

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
    def cooking_time(self) -> int:
        pass

    @abc.abstractmethod
    def prepare(self) -> None:
        pass

    def bake(self) -> None:
        print(f"[{self.name}] 조리 시간: {self.cooking_time} 분")

    def cut(self) -> None:
        print(f"[{self.name}] 자름")

    def box(self) -> None:
        print(f"[{self.name}] 상자에 담음")
