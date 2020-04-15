from .interfaces import Command
from .remote_objects import Light


class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light = light

    def __repr__(self) -> str:
        return "turn on the light"

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light = light

    def __repr__(self) -> str:
        return "turn off the light"

    def execute(self) -> None:
        self.light.off()

    def undo(self) -> None:
        self.light.on()
