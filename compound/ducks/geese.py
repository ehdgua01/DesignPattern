from .interfaces import Goose


class LandesGoose(Goose):
    def honk(self) -> None:
        print("꽥")
