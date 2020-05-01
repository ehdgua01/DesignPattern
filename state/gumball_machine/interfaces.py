import abc


class Machine(abc.ABC):
    @abc.abstractmethod
    def insert_quarter(self) -> None:
        pass

    @abc.abstractmethod
    def eject_quarter(self) -> None:
        pass

    @abc.abstractmethod
    def turn_crank(self) -> None:
        pass

    @abc.abstractmethod
    def set_state(self, state: "State") -> None:
        pass

    @abc.abstractmethod
    def release_ball(self) -> None:
        pass


class State(abc.ABC):
    def __init__(self, machine: Machine):
        self.machine = machine

    @abc.abstractmethod
    def insert_quarter(self) -> None:
        pass

    @abc.abstractmethod
    def eject_quarter(self) -> None:
        pass

    @abc.abstractmethod
    def turn_crank(self) -> None:
        pass

    @abc.abstractmethod
    def dispense(self) -> None:
        pass
