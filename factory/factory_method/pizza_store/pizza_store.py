"""
Simulation of factory method pattern
>>> korea_factory = KoreaPizzaFactory()
>>> america_factory = AmericaPizzaFactory()
>>> america_factory.order(Base.CHEESE)
[치즈 피자] 반죽: 밀가루, 소스: 치즈 피자 소스, 토핑: 치즈
[치즈 피자] 조리 시간: 10 분
[치즈 피자] 자름
[치즈 피자] 상자에 담음
>>> korea_factory.order(AmericaPizza.CHICAGO)
Traceback (most recent call last):
 ...
ValueError: 없는 피자 종류입니다.
>>> korea_factory.order(KoreaPizza.BULGOGI)
[불고기 피자] 반죽: 밀가루, 소스: 불고기 피자 소스, 토핑: 불고기, 올리브
[불고기 피자] 조리 시간: 15 분
[불고기 피자] 자름
[불고기 피자] 상자에 담음
>>> korea_factory.order(Base.PEPPERONI)
[페퍼로니 피자] 반죽: 밀가루, 소스: 페퍼로니 피자 소스, 토핑: 페퍼로니
[페퍼로니 피자] 조리 시간: 10 분
[페퍼로니 피자] 자름
[페퍼로니 피자] 상자에 담음
>>> america_factory.order(AmericaPizza.CHICAGO)
[시카고 피자] 반죽: 밀가루, 소스: 시카고 피자 소스, 토핑: 치즈, 치즈, 치즈
[시카고 피자] 조리 시간: 20 분
[시카고 피자] 자름
[시카고 피자] 상자에 담음
"""
from .pizza_store_abc import Pizza, PizzaFactory, PIZZA
from .pizza_type import (
    KoreaPizzaType,
    AmericaPizzaType,
    KoreaPizza,
    AmericaPizza,
    Base,
)


class BulgogiPizza(Pizza):
    name = "불고기 피자"
    dough = "밀가루"
    sauce = "불고기 피자 소스"
    toppings = ["불고기", "올리브"]
    cooking_time = 15


class ChicagoPizza(Pizza):
    name = "시카고 피자"
    dough = "밀가루"
    sauce = "시카고 피자 소스"
    toppings = ["치즈", "치즈", "치즈"]
    cooking_time = 20


class CheesePizza(Pizza):
    name = "치즈 피자"
    dough = "밀가루"
    sauce = "치즈 피자 소스"
    toppings = ["치즈"]
    cooking_time = 10


class PepperoniPizza(Pizza):
    name = "페퍼로니 피자"
    dough = "밀가루"
    sauce = "페퍼로니 피자 소스"
    toppings = ["페퍼로니"]
    cooking_time = 10


class KoreaPizzaFactory(PizzaFactory):
    def order(self, pizza_type: KoreaPizzaType) -> None:
        super().order(pizza_type)

    def create_pizza(self, pizza_type: KoreaPizzaType) -> PIZZA:
        if pizza_type == KoreaPizza.BULGOGI:
            return BulgogiPizza()
        elif pizza_type == Base.PEPPERONI:
            return PepperoniPizza()
        elif pizza_type == Base.CHEESE:
            return CheesePizza()  # pragma: no cover
        else:
            raise ValueError("없는 피자 종류입니다.")


class AmericaPizzaFactory(PizzaFactory):
    def order(self, pizza_type: AmericaPizzaType) -> None:
        super().order(pizza_type)

    def create_pizza(self, pizza_type: AmericaPizzaType) -> PIZZA:
        if pizza_type == AmericaPizza.CHICAGO:
            return ChicagoPizza()
        elif pizza_type == Base.PEPPERONI:
            return PepperoniPizza()  # pragma: no cover
        elif pizza_type == Base.CHEESE:
            return CheesePizza()
        else:
            raise ValueError("없는 피자 종류입니다.")  # pragma: no cover
