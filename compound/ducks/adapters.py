from .interfaces import Quackable, Goose


class GooseAdapter(Quackable):
    def __init__(self, goose: Goose) -> None:
        self.goose = goose

    def quack(self) -> None:
        self.goose.honk()
