import os

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QComboBox, QListWidget, QColorDialog

from src.model.command.invoker import Invoker
from src.model.figure.baseFigureActions import BaseFigureActions
from src.model.figure.figure import Figure
from src.model.figure.figureType import FigureType
from src.model.memento.caretaker import Caretaker
from src.model.proxy.loggerProxy import LoggerProxy

uiFile = os.getcwd() + "/src/View/mainWindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        figureSize = 50

        self._figure: BaseFigureActions = Figure(self.figure_graphics_view, figureSize)
        proxy = LoggerProxy(self.logs_list_view, self._figure)

        self._invoker = Invoker(proxy)
        self._caretaker = Caretaker(proxy)

        self._caretaker.save()
        self._figure.draw()

        self.size_selector.setValue(figureSize)

        self._init_figure_types()
        self._set_connections()

    def _on_distroed(self):
        self._appModel.disconnect()

    def _init_figure_types(self):
        for figureType in FigureType:
            self.figure_type_selector.addItem(figureType.value)

    def _set_connections(self):
        self.figure_type_selector.currentTextChanged.connect(self.figureTypeChanged)
        self.size_selector.valueChanged.connect(self.figureSizeChanged)
        self.border_thickness_selector.valueChanged.connect(self.figureBoredThicknessChanged)
        self.undo_btn.clicked.connect(lambda x: self._caretaker.undo())
        self.clear_logs_btn.clicked.connect(lambda x: self.logs_list_view.clear())
        self.save_logs_btn.clicked.connect(self.saveLogs)
        self.change_border_color_btn.clicked.connect(lambda x: self.changeColor('border'))
        self.change_figure_btn.clicked.connect(lambda x: self.changeColor('fill'))

    def about(self):
        QMessageBox.about(self, "About", "Ametov Pavel\n8-T3O-302B-16")

    def figureTypeChanged(self, text):
        self._caretaker.save()
        self._invoker.changeFigureType(FigureType[text])

    def figureSizeChanged(self, value):
        self._caretaker.save()
        self._invoker.changeSize(value)

    def saveLogs(self):
        QListWidget().count()

        with open('figure.autosave', 'w+') as file:
            for item in self.logs_list_view.findItems("*", Qt.MatchWildcard):
                file.write(item.text() + '\n')

    def figureBoredThicknessChanged(self, value):
        self._caretaker.save()
        self._invoker.changeBorderThickness(value)

    def changeColor(self, value):
        color = QColorDialog.getColor(Qt.white)

        if not color.isValid():
            return

        if value == 'fill':
            self._invoker.changeFillColor(color)
        else:
            pass
            self._invoker.changeBorderColor(color)

        self._caretaker.save()

    @staticmethod
    def error(message: str):
        box = QMessageBox()
        box.setWindowTitle("Error")
        box.setText(message)
        box.exec()