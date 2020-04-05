import math

from PyQt5.QtGui import QColor, QPixmap, QPainter, QBrush, QPen, QPainterPath
from PyQt5.QtWidgets import QLabel

from src.model.figure.baseFigureActions import BaseFigureActions
from src.model.figure.figureType import FigureType
from src.model.memento.baseMemento import BaseMemento
from src.model.memento.figureMemento import FigureMemento


class Figure(BaseFigureActions):
    def __init__(self, view: QLabel, size: int = 40, width: int = 300, height: int = 300):
        self._view = view
        self._type: FigureType = FigureType.Circle
        self._color = QColor().fromRgb(255, 255, 255)
        self._borderColor = QColor().fromRgb(0, 0, 0)
        self._borderThickness = 1
        self._size = size
        self._width = width
        self._height = height

        self._figuresDraw = {
            FigureType.Circle: self.drawCircle,
            FigureType.RegularHexagon: self.drawRegularHexagon,
            FigureType.RegularPentagon: self.drawRegularPentagon,
            FigureType.RegularTriangle: self.drawRegularTriangle,
            FigureType.Square: self.drawSquare,
        }

    def changeBorderColor(self, color: QColor):
        self._borderColor = color
        self.draw()

    def changeBorderThickness(self, thickness: int):
        self._borderThickness = thickness
        self.draw()

    def changeFigureType(self, figureType: FigureType):
        self._type = figureType
        self.draw()

    def changeFillColor(self, color: QColor):
        self._color = color
        self.draw()

    def changeSize(self, size: int):
        self._size = size
        self.draw()

    def save(self) -> BaseMemento:
        return FigureMemento(self._borderColor,
                             self._borderThickness,
                             self._color,
                             self._size,
                             self._type)

    def restore(self, memento: BaseMemento):
        self._type = memento.getFigureType()
        self._color = memento.getFillColor()
        self._borderColor = memento.getBorderColor()
        self._borderThickness = memento.getBorderThickness()
        self._size = memento.getSize()

        self.draw()

    def draw(self):
        colorWhite = QColor().fromRgb(255, 255, 255)

        pixmap = QPixmap(self._width, self._height)
        pixmap.fill(colorWhite)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillRect(0, 0, self._width, self._height, QBrush(colorWhite))
        painter.setPen(QPen(self._borderColor, self._borderThickness))
        painter.setBrush(QBrush(self._color))

        drawer = self._figuresDraw.get(self._type)
        if painter is None:
            raise Exception('Draw not set')

        drawer(painter)

        painter.end()

        self._view.setPixmap(pixmap)
        self._view.setMinimumSize(self._width, self._height)

    def drawCircle(self, painter: QPainter):
        painter.drawEllipse((self._width / 2) - self._size, (self._height / 2) - self._size, self._size * 2, self._size * 2)

    def drawRegularTriangle(self, painter: QPainter):
        self.drawPath(painter, 3)

    def drawSquare(self, painter: QPainter):
        sqrt = math.sqrt(2)
        delta = self._size / sqrt
        painter.drawRect((self._width / 2) - delta, (self._height / 2) - delta, delta * 2, delta * 2)

    def drawRegularPentagon(self, painter: QPainter):
        self.drawPath(painter, 5)

    def drawRegularHexagon(self, painter: QPainter):
        self.drawPath(painter, 6)

    def drawPath(self, painter: QPainter, pointsAmount: int):
        angel = (2 * math.pi) / pointsAmount
        centerX = self._width / 2
        centerY = self._height / 2

        path = QPainterPath()

        path.moveTo(centerX + self._size, centerY + self._size)

        cos = math.cos(angel)
        sin = math.sin(angel)

        x = centerX
        y = centerY

        for i in range(pointsAmount):
            newX = x * cos - y * sin
            newY = x * sin + y * cos

            x = newX
            y = newY

            path.lineTo(centerX + x, centerY + y)

        painter.drawPath(path)
