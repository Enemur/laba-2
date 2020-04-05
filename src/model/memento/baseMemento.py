from abc import ABC, abstractmethod


class BaseMemento(ABC):
    @abstractmethod
    def getFigureType(self):
        pass

    @abstractmethod
    def getBorderColor(self):
        pass

    @abstractmethod
    def getBorderThickness(self):
        pass

    @abstractmethod
    def getFillColor(self):
        pass

    @abstractmethod
    def getSize(self):
        pass
