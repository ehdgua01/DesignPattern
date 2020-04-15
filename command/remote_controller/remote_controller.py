"""
Simulation of command pattern

>>> from .remote_objects import Light
>>> from .commands import LightOnCommand, LightOffCommand
>>> controller = RemoteController()
>>> light = Light()
>>> controller.set_command(2, LightOnCommand(light), LightOffCommand(light))
>>> controller.on(0)
no command
>>> controller.off(0)
no command
>>> controller.undo()
no command
>>> controller.on(2)
>>> light.light
True
>>> controller.off(2)
>>> light.light
False
>>> controller.undo()
>>> light.light
True
>>> controller.on(2)
>>> controller.undo()
>>> light.light
False
>>> controller.help()
[slot 2] on: turn on the light, off: turn off the light
<BLANKLINE>
"""
from typing import Dict, List

from .interfaces import CommandType


class RemoteController(object):
    def __init__(self) -> None:
        self.slots: Dict[int, Dict[str, CommandType]] = {}
        self.history: List[CommandType] = []

    def set_command(
        self, slot: int, on_command: CommandType, off_command: CommandType
    ) -> None:
        self.slots[slot] = {
            "on": on_command,
            "off": off_command,
        }

    def on(self, slot: int) -> None:
        if slot not in self.slots:
            print("no command")
            return

        command = self.slots[slot]["on"]
        command.execute()
        self.history.append(command)

    def off(self, slot: int) -> None:
        if slot not in self.slots:
            print("no command")
            return

        command = self.slots[slot]["off"]
        command.execute()
        self.history.append(command)

    def undo(self) -> None:
        if not len(self.history):
            print("no command")
            return

        self.history.pop().undo()

    def help(self) -> None:
        text = ""

        for slot, commands in self.slots.items():
            text += (
                f"[slot {slot}] on: {commands['on']}, off: {commands['off']}\n"
            )

        print(text)
