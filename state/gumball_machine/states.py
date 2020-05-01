import random

from .interfaces import State


class HasQuarterState(State):
    def insert_quarter(self) -> None:
        print("동전은 한 개만 넣어주세요.")

    def eject_quarter(self) -> None:
        print("동전이 반환됩니다.")
        self.machine.set_state(self.machine.no_quarter_state)

    def turn_crank(self) -> None:
        print("손잡이를 돌리셨습니다.")
        winner = random.randint(0, 9)
        if winner == 0:
            self.machine.set_state(self.machine.winner_state)
        else:
            self.machine.set_state(self.machine.sold_state)

    def dispense(self) -> None:
        print("알맹이가 나갈 수 없습니다.")


class NoQuarterState(State):
    def insert_quarter(self) -> None:
        print("동전을 넣으셨습니다.")
        self.machine.set_state(self.machine.has_quarter_state)

    def eject_quarter(self) -> None:
        print("동전을 넣어주세요.")

    def turn_crank(self) -> None:
        print("동전을 넣어주세요.")

    def dispense(self) -> None:
        print("동전을 넣어주세요.")


class SoldOutState(State):
    def insert_quarter(self) -> None:
        print("매진되었습니다. 다음 기회에 이용해주세요.")

    def eject_quarter(self) -> None:
        print("동전을 넣어주세요.")

    def turn_crank(self) -> None:
        print("매진되었습니다. 다음 기회에 이용해주세요.")

    def dispense(self) -> None:
        print("매진되었습니다. 다음 기회에 이용해주세요.")


class SoldState(State):
    def insert_quarter(self) -> None:
        print("잠시만 기다려 주세요. 알맹이가 나가고 있습니다.")

    def eject_quarter(self) -> None:
        print("이미 알맹이를 뽑으셨습니다.")

    def turn_crank(self) -> None:
        print("손잡이는 한 번만 돌려주세요.")

    def dispense(self) -> None:
        print("알맹이가 나가고 있습니다.")
        self.machine.release_ball()
        if 0 < self.machine.count:
            self.machine.set_state(self.machine.no_quarter_state)
        else:
            self.machine.set_state(self.machine.sold_out_state)


class WinnerState(State):
    def insert_quarter(self) -> None:
        print("잠시만 기다려 주세요. 알맹이가 나가고 있습니다.")

    def eject_quarter(self) -> None:
        print("이미 알맹이를 뽑으셨습니다.")

    def turn_crank(self) -> None:
        print("손잡이는 한 번만 돌려주세요.")

    def dispense(self) -> None:
        print("축하드립니다, 알맹이를 하나 더 받으실 수 있습니다.")
        self.machine.release_ball()
        if 0 < self.machine.count:
            self.machine.set_state(self.machine.no_quarter_state)
        else:
            self.machine.release_ball()
            if 0 < self.machine.count:
                self.machine.set_state(self.machine.no_quarter_state)
            else:
                self.machine.set_state(self.machine.sold_out_state)
