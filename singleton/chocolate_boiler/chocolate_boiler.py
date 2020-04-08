"""
Simulation Singleton pattern
>>> boiler1 = ChocolateBoiler()
>>> boiler2 = ChocolateBoiler()
>>> id(boiler1) == id(boiler2)
True
>>> boiler1.boil()
재료가 없음
>>> boiler2.drain()
작업 중인 재료가 없음
>>> boiler1.fill()
재료를 집어넣음
>>> boiler2.fill()
이미 재료가 차있음
>>> boiler1.drain()
끓이기 작업이 안 끝남
>>> boiler2.boil()
재료를 끓이는 중
>>> boiler1.boil()
다른 재료 끓이는 중
>>> boiler1.drain()
완제품 수거
>>> import threading
>>> threads = []
>>> for _ in range(5):
...     thr = threading.Thread(
...         target=lambda : print(id(boiler1) == id(ChocolateBoiler()))
...     )
...     threads.append(thr)
...     thr.start()
True
True
True
True
True
"""


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class ChocolateBoiler(Singleton):
    __empty = True
    __boiled = False

    def fill(self) -> None:
        if self.is_empty():
            self.__empty = False
            self.__boiled = False
            print("재료를 집어넣음")
        else:
            print("이미 재료가 차있음")

    def drain(self) -> None:
        if not self.is_empty() and self.is_boiled():
            self.__empty = True
            print("완제품 수거")
        elif self.is_empty():
            print("작업 중인 재료가 없음")
        else:
            print("끓이기 작업이 안 끝남")

    def boil(self) -> None:
        if not self.is_empty() and not self.is_boiled():
            print("재료를 끓이는 중")
            self.__boiled = True
        elif self.is_empty():
            print("재료가 없음")
        else:
            print("다른 재료 끓이는 중")

    def is_empty(self) -> bool:
        return self.__empty

    def is_boiled(self) -> bool:
        return self.__boiled
