from src.model.command.baseCommand import Command
from src.model.figure.baseFigureActions import BaseFigureActions


class ChangeBorderThickness(Command):
    def __init__(self, figureActions: BaseFigureActions, thickness: int):
        self._figureActions = figureActions
        self._thickness = thickness

    def execute(self):
        self._figureActions.changeBorderThickness(self._thickness)
