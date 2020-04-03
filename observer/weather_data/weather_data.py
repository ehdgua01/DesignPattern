"""
This simulation is intended to obtain weather data.
>>> weather_station = SubjectWeather()
>>> display = ConditionsDisplay(weather_station)
>>> weather_station.set_data({
...     'temperature': 80,
...     'humidity': 70,
...     'pressure': 29.2,
... })
{'temperature': 80, 'humidity': 70, 'pressure': 29.2}
>>> weather_station.set_data({
...     'temperature': 60,
...     'humidity': 50,
...     'pressure': 30.2,
... })
{'temperature': 60, 'humidity': 50, 'pressure': 30.2}
"""
from asyncio import new_event_loop, wait
from typing import List

from .observer_abc import Observer, Subject, DisplayElement
from .weather_typing import WEATHER_DATA


class SubjectWeather(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.__observers: List[Observer] = []
        self.__data: WEATHER_DATA = {}
        self.__event_loop = new_event_loop()

    def register_observer(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify_observers(self) -> None:
        self.__event_loop.run_until_complete(
            wait([o.update(self.__data) for o in self.__observers]),
        )

    def measurements_changed(self) -> None:
        self.notify_observers()

    def set_data(self, data: WEATHER_DATA) -> None:
        self.__data.update(data)
        self.measurements_changed()


class ConditionsDisplay(Observer, DisplayElement):
    def __init__(self, subject: SubjectWeather) -> None:
        self.__data: WEATHER_DATA = {}
        self.__subject = subject
        self.__subject.register_observer(self)

    async def update(self, data: WEATHER_DATA) -> None:
        self.__data.update(data)
        self.display()

    def display(self) -> None:
        print(self.__data)
