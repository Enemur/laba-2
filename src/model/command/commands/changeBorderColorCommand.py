from PyQt5.QtGui import QColor

from src.model.command.baseCommand import Command
from src.model.figure.baseFigureActions import BaseFigureActions


class ChangeBorderColorCommand(Command):
    def __init__(self, figureActions: BaseFigureActions, color: QColor):
        self._figureActions = figureActions
        self._color = color

    def execute(self):
        self._figureActions.changeBorderColor(self._color)
