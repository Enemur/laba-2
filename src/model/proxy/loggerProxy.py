from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QListWidget

from src.model.figure.figureType import FigureType
from src.model.memento.baseMemento import BaseMemento
from src.model.figure.baseFigureActions import BaseFigureActions


class LoggerProxy(BaseFigureActions):
    def __init__(self, view: QListWidget, figureActions: BaseFigureActions):
        self._view: QListWidget = view
        self._figureActions = figureActions

    def changeBorderColor(self, color: QColor):
        self._figureActions.changeBorderColor(color)
        self._view.addItem('Border color changed')

    def changeBorderThickness(self, thickness: int):
        self._figureActions.changeBorderThickness(thickness)
        self._view.addItem('Thickness changed')

    def changeFigureType(self, figureType: FigureType):
        self._figureActions.changeFigureType(figureType)
        self._view.addItem('Type changed')

    def changeFillColor(self, color: QColor):
        self._figureActions.changeFillColor(color)
        self._view.addItem('Color changed')

    def changeSize(self, size: int):
        self._figureActions.changeSize(size)
        self._view.addItem('Size changed')

    def save(self) -> BaseMemento:
        memento = self._figureActions.save()
        return memento

    def restore(self, memento: BaseMemento):
        self._figureActions.restore(memento)

    def draw(self):
        self._figureActions.draw()

