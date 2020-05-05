import abc


class Quackable(abc.ABC):
    @abc.abstractmethod
    def quack(self) -> None:
        pass


class Goose(abc.ABC):
    @abc.abstractmethod
    def honk(self) -> None:
        pass
