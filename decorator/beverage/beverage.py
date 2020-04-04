"""
>>> print(espresso_with_mocha())
(2000, '에스프레소, 모카')
>>> print(espresso_with_double_mocha())
(2500, '에스프레소, 모카, 모카')
>>> print(dark_roast_with_whip())
(2500, '다크로스트, 휘핑')
>>> print(house_blend_with_soy_and_steam_milk())
(3000, '하우스블렌드, 두유, 스팀밀크')
"""
from functools import wraps
from typing import Tuple


RETURN_TYPE = Tuple[int, str]


def espresso() -> RETURN_TYPE:
    return 1500, "에스프레소"


def house_blend() -> RETURN_TYPE:
    return 2000, "하우스블렌드"


def dark_roast() -> RETURN_TYPE:
    return 2000, "다크로스트"


def mocha(beverage):
    @wraps(beverage)
    def wrapper() -> RETURN_TYPE:
        cost, description = beverage()
        return cost + 500, f"{description}, 모카"

    return wrapper


def whip(beverage):
    @wraps(beverage)
    def wrapper() -> RETURN_TYPE:
        cost, description = beverage()
        return cost + 500, f"{description}, 휘핑"

    return wrapper


def soy(beverage):
    @wraps(beverage)
    def wrapper() -> RETURN_TYPE:
        cost, description = beverage()
        return cost + 500, f"{description}, 두유"

    return wrapper


def steam_milk(beverage):
    @wraps(beverage)
    def wrapper() -> RETURN_TYPE:
        cost, description = beverage()
        return cost + 500, f"{description}, 스팀밀크"

    return wrapper


@mocha
def espresso_with_mocha() -> RETURN_TYPE:
    return espresso()


@mocha
@mocha
def espresso_with_double_mocha() -> RETURN_TYPE:
    return espresso()


@whip
def dark_roast_with_whip() -> RETURN_TYPE:
    return dark_roast()


@steam_milk
@soy
def house_blend_with_soy_and_steam_milk() -> RETURN_TYPE:
    return house_blend()
