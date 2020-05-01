from .interfaces import State, Machine
from .states import (
    HasQuarterState,
    NoQuarterState,
    SoldOutState,
    SoldState,
    WinnerState,
)


class GumballMachine(Machine):
    def __init__(self, count: int) -> None:
        self.has_quarter = HasQuarterState(self)
        self.no_quarter = NoQuarterState(self)
        self.sold_out = SoldOutState(self)
        self.sold = SoldState(self)
        self.winner = WinnerState(self)
        self.state: State = self.sold_out
        self.count = count

        if 0 < count:
            self.state = self.no_quarter

    def insert_quarter(self) -> None:
        self.state.insert_quarter()

    def eject_quarter(self) -> None:
        self.state.eject_quarter()

    def turn_crank(self) -> None:
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state: State) -> None:
        self.state = state

    def release_ball(self) -> None:
        if 0 < self.count:
            self.count -= 1

    @property
    def has_quarter_state(self) -> HasQuarterState:
        return self.has_quarter

    @property
    def no_quarter_state(self) -> NoQuarterState:
        return self.no_quarter

    @property
    def sold_out_state(self) -> SoldOutState:
        return self.sold_out

    @property
    def sold_state(self) -> SoldState:
        return self.sold

    @property
    def winner_state(self) -> WinnerState:
        return self.winner
