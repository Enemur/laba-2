from src.model.command.baseCommand import Command
from src.model.figure.baseFigureActions import BaseFigureActions


class ChangeSizeCommand(Command):
    def __init__(self, figureActions: BaseFigureActions, size: int):
        self._figureActions = figureActions
        self._size = size

    def execute(self):
        self._figureActions.changeSize(self._size)
