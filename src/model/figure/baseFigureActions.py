from abc import ABC, abstractmethod
from PyQt5.QtGui import QColor
from src.model.figure.figureType import FigureType
from src.model.memento.baseMemento import BaseMemento


class BaseFigureActions(ABC):
    @abstractmethod
    def changeBorderColor(self, color: QColor):
        pass

    @abstractmethod
    def changeBorderThickness(self, thickness: int):
        pass

    @abstractmethod
    def changeFigureType(self, figureType: FigureType):
        pass

    @abstractmethod
    def changeFillColor(self, color: QColor):
        pass

    @abstractmethod
    def changeSize(self, size: int):
        pass

    @abstractmethod
    def save(self) -> BaseMemento:
        pass

    @abstractmethod
    def restore(self, memento: BaseMemento):
        pass

    @abstractmethod
    def draw(self):
        pass
