import abc

from .weather_typing import WEATHER_DATA


class Observer(abc.ABC):
    @abc.abstractmethod
    async def update(self, data: WEATHER_DATA) -> None:
        pass


class Subject(abc.ABC):
    @abc.abstractmethod
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abc.abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abc.abstractmethod
    def notify_observers(self) -> None:
        pass


class DisplayElement(abc.ABC):
    @abc.abstractmethod
    def display(self) -> None:
        pass
