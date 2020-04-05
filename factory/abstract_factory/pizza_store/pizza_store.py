"""
Simulation of Abstract Factory Pattern
>>> pizza_store = KoreaPizzaStore()
>>> pizza_store.order(PizzaType.BULGOGI)
[불고기 피자] 반죽: 밀가루 반죽, 소스: 불고기 피자 소스, 불고기: 매운 불고기
[불고기 피자] 조리 시간: 20 분
[불고기 피자] 자름
[불고기 피자] 상자에 담음
>>> pizza_store.order(PizzaType.CHEESE)
[치즈 피자] 반죽: 밀가루 반죽, 소스: 치즈 피자 소스, 치즈: 신선한 치즈
[치즈 피자] 조리 시간: 10 분
[치즈 피자] 자름
[치즈 피자] 상자에 담음
>>> pizza_store.order('')
Traceback (most recent call last):
 ...
ValueError: 없는 피자 종류입니다.
"""
from .pizza_store_abc import PizzaStore
from .pizza_abc import Pizza, PIZZA
from .ingredient_abc import (
    IngredientFactory,
    INGREDIENT_FACTORY,
    Bulgogi,
    Cheese,
    Dough,
    BULGOGI,
    CHEESE,
    DOUGH,
)
from .pizza_type import PizzaType


class BulgogiPizza(Pizza):
    name = "불고기 피자"
    cooking_time = 20
    sauce = '불고기 피자 소스'

    def __init__(self, ingredient_factory: INGREDIENT_FACTORY) -> None:
        super().__init__()
        self.factory = ingredient_factory

    def prepare(self) -> None:
        self.dough = self.factory.create_dough()
        self.bulgogi = self.factory.create_bulgogi()
        print(
            f"[{self.name}] "
            f"반죽: {self.dough.name}, "
            f"소스: {self.sauce}, "
            f"불고기: {self.bulgogi.name}"
        )


class CheesePizza(Pizza):
    name = "치즈 피자"
    cooking_time = 10
    sauce = '치즈 피자 소스'

    def __init__(self, ingredient_factory: INGREDIENT_FACTORY) -> None:
        super().__init__()
        self.factory = ingredient_factory

    def prepare(self) -> None:
        self.dough = self.factory.create_dough()
        self.cheese = self.factory.create_cheese()
        print(
            f"[{self.name}] "
            f"반죽: {self.dough.name}, "
            f"소스: {self.sauce}, "
            f"치즈: {self.cheese.name}"
        )


class HotBulgogi(Bulgogi):
    name = "매운 불고기"


class FreshCheese(Cheese):
    name = "신선한 치즈"


class FlourDough(Dough):
    name = "밀가루 반죽"


class KoreaIngredientFactory(IngredientFactory):
    def create_bulgogi(self) -> BULGOGI:
        return HotBulgogi()

    def create_cheese(self) -> CHEESE:
        return FreshCheese()

    def create_dough(self) -> DOUGH:
        return FlourDough()


class KoreaPizzaStore(PizzaStore):
    def __init__(self) -> None:
        self.factory: INGREDIENT_FACTORY = KoreaIngredientFactory()

    def order(self, pizza_type: PizzaType) -> None:
        super().order(pizza_type)

    def create_pizza(self, pizza_type: PizzaType) -> PIZZA:
        if pizza_type == PizzaType.BULGOGI:
            return BulgogiPizza(self.factory)
        elif pizza_type == PizzaType.CHEESE:
            return CheesePizza(self.factory)
        else:
            raise ValueError("없는 피자 종류입니다.")
