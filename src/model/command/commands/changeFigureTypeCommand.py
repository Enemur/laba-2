from src.model.command.baseCommand import Command
from src.model.figure.baseFigureActions import BaseFigureActions
from src.model.figure.figureType import FigureType


class ChangeFigureTypeCommand(Command):
    def __init__(self, figureActions: BaseFigureActions, figureType: FigureType):
        self._figureActions = figureActions
        self._figureType = figureType

    def execute(self):
        self._figureActions.changeFigureType(self._figureType)
