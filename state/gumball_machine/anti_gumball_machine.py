class GumballMachine(object):
    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3

    def __init__(self, count: int) -> None:
        self.state = self.SOLD_OUT
        self.count = count

        if 0 < count:
            self.state = self.NO_QUARTER

    def insert_quarter(self) -> None:
        if self.state == self.HAS_QUARTER:
            print("동전은 한 개만 넣어주세요.")
        elif self.state == self.NO_QUARTER:
            print("동전을 넣으셨습니다.")
        elif self.state == self.SOLD_OUT:
            print("매진되었습니다. 다음 기회에 이용해주세요.")
        elif self.state == self.SOLD:
            print("잠시만 기다려 주세요. 알맹이가 나가고 있습니다.")

    def eject_quarter(self) -> None:
        if self.state == self.HAS_QUARTER:
            print("동전이 반환됩니다.")
            self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print("동전을 넣어주세요.")
        elif self.state == self.SOLD_OUT:
            print("동전을 넣어주세요.")
        elif self.state == self.SOLD:
            print("이미 알맹이를 뽑으셨습니다.")

    def turn_crank(self) -> None:
        if self.state == self.HAS_QUARTER:
            print("손잡이를 돌리셨습니다.")
            self.state = self.SOLD
            self.dispense()
        elif self.state == self.NO_QUARTER:
            print("동전을 넣어주세요.")
        elif self.state == self.SOLD_OUT:
            print("매진되었습니다. 다음 기회에 이용해주세요.")
        elif self.state == self.SOLD:
            print("손잡이는 한 번만 돌려주세요.")

    def dispense(self) -> None:
        if self.state == self.HAS_QUARTER:
            print("알맹이가 나갈 수 없습니다.")
        elif self.state == self.NO_QUARTER:
            print("동전을 넣어주세요.")
        elif self.state == self.SOLD_OUT:
            print("매진되었습니다. 다음 기회에 이용해주세요.")
        elif self.state == self.SOLD:
            print("알맹이가 나가고 있습니다.")
            self.count -= 1
            if self.count == 0:
                print("매진되었습니다.")
                self.state = self.SOLD_OUT
            else:
                self.state = self.NO_QUARTER
