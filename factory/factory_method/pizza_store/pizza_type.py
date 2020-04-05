import enum
from typing import Union


@enum.unique
class Base(enum.Enum):
    CHEESE = "치즈"
    PEPPERONI = "페퍼로니"


@enum.unique
class KoreaPizza(enum.Enum):
    BULGOGI = "불고기"


@enum.unique
class AmericaPizza(enum.Enum):
    CHICAGO = "시카고"


KoreaPizzaType = Union[KoreaPizza, Base]
AmericaPizzaType = Union[AmericaPizza, Base]
