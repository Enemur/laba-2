from src.model.memento.baseMemento import BaseMemento


class FigureMemento(BaseMemento):
    def __init__(self, borderColor, borderThickness, fillColor, size, figureType):
        self._borderColor = borderColor
        self._borderThickness = borderThickness
        self._fillColor = fillColor
        self._size = size
        self._figureType = figureType

    def getBorderColor(self):
        return self._borderColor

    def getBorderThickness(self):
        return self._borderThickness

    def getFillColor(self):
        return self._fillColor

    def getSize(self):
        return self._size

    def getFigureType(self):
        return self._figureType
