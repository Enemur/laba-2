from src.model.command.baseCommand import Command


class MacroCommand(Command):
    def __init__(self, commands: [Command]):
        self._commands = commands

    def execute(self):
        for command in self._commands:
            command.execute()
