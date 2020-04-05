import abc
from typing import TypeVar


CHEESE = TypeVar("CHEESE", bound="Cheese")
DOUGH = TypeVar("DOUGH", bound="Dough")
BULGOGI = TypeVar("BULGOGI", bound="Bulgogi")
INGREDIENT_FACTORY = TypeVar("INGREDIENT_FACTORY", bound="IngredientFactory")


class Cheese(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass


class Dough(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass


class Bulgogi(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass


class IngredientFactory(abc.ABC):
    @abc.abstractmethod
    def create_cheese(self) -> CHEESE:
        pass

    @abc.abstractmethod
    def create_dough(self) -> DOUGH:
        pass

    @abc.abstractmethod
    def create_bulgogi(self) -> BULGOGI:
        pass
