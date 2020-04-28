from .interfaces import Duck, Turkey


class MallardDuck(Duck):
    def quack(self) -> None:
        print("물오리: 꽥")

    def fly(self) -> None:
        print("물오리: 나는 중(장거리)")


class WildTurkey(Turkey):
    def gobble(self) -> None:
        print("칠면조: 골골")

    def fly(self) -> None:
        print("칠면조: 나는 중(단거리)")
