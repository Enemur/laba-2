from src.model.figure.baseFigureActions import BaseFigureActions
from src.model.memento.baseMemento import BaseMemento


class Caretaker:
    def __init__(self, figureActions: BaseFigureActions):
        self._figureActions = figureActions
        self._mementos: [BaseMemento] = []

    def save(self):
        self._mementos.append(self._figureActions.save())

    def undo(self):
        if len(self._mementos) == 0:
            return

        memento = self._mementos.pop()

        self._figureActions.restore(memento)
