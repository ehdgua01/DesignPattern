import abc


class Duck(abc.ABC):
    @abc.abstractmethod
    def quack(self) -> None:
        pass

    @abc.abstractmethod
    def fly(self) -> None:
        pass


class Turkey(abc.ABC):
    @abc.abstractmethod
    def gobble(self) -> None:
        pass

    @abc.abstractmethod
    def fly(self) -> None:
        pass
