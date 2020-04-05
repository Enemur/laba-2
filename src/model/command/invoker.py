from PyQt5.QtGui import QColor

from src.model.command.commands.changeBorderColorCommand import ChangeBorderColorCommand
from src.model.command.commands.changeBorderThicknessCommand import ChangeBorderThickness
from src.model.command.commands.changeFigureTypeCommand import ChangeFigureTypeCommand
from src.model.command.commands.changeFillColorCommand import ChangeFillColorCommand
from src.model.command.commands.changeSizeCommand import ChangeSizeCommand
from src.model.figure.baseFigureActions import BaseFigureActions
from src.model.figure.figureType import FigureType


class Invoker:
    def __init__(self, figureActions: BaseFigureActions):
        self._figureActions = figureActions

    def changeBorderColor(self, color: QColor):
        command = ChangeBorderColorCommand(self._figureActions, color)
        command.execute()

    def changeBorderThickness(self, thickness: int):
        command = ChangeBorderThickness(self._figureActions, thickness)
        command.execute()

    def changeFigureType(self, figureType: FigureType):
        command = ChangeFigureTypeCommand(self._figureActions, figureType)
        command.execute()

    def changeFillColor(self, color: QColor):
        command = ChangeFillColorCommand(self._figureActions, color)
        command.execute()

    def changeSize(self, size: int):
        command = ChangeSizeCommand(self._figureActions, size)
        command.execute()
