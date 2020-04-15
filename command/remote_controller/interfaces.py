import abc
from typing import TypeVar


class Command(abc.ABC):
    @abc.abstractmethod
    def __repr__(self) -> str:
        pass

    @abc.abstractmethod
    def execute(self) -> None:
        pass

    @abc.abstractmethod
    def undo(self) -> None:
        pass


CommandType = TypeVar("CommandType", bound=Command)
