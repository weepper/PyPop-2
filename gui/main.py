import sys
import json
from PyQt5.QtWidgets import QMainWindow, QMenu, QLabel, QPushButton, QWidget, QScrollArea, QVBoxLayout, QHBoxLayout

from gui.param import paramWindow
from gui.widgets import FlowLayout, previewWidget
#from app import setting

class mainWindow(QMainWindow):
    def __init__(self, app):
        super(mainWindow, self).__init__()

        self.paramW = None
        self.screen = [app.primaryScreen().size().width(), app.primaryScreen().size().height()]
        self.setWindowTitle("PyPop")

        self._createMenuBar()

        self.mainLayout = QVBoxLayout()

        self.grid = FlowLayout()
        self.grid.setContentsMargins(0,0,0,0)
        for i in range(5):
            self.grid.addWidget(previewWidget())

        self.scroll = QScrollArea(self)
        self.scroll.setWidget(self.grid.asWidget())
        self.scroll.setWidgetResizable(True)

        self.setCentralWidget(self.scroll)
    
    def _createMenuBar(self):
        self.menu = self.menuBar()
        optionMenu = QMenu("&Option", self)
        optionMenu.addAction("parameter", self.openParameter)
        optionMenu.addAction("quit", self.close)
        self.menu.addMenu(optionMenu)

    def openParameter(self):
        if self.paramW is None:
            self.paramW = paramWindow(self.screen)
        self.paramW.show()

    def close(self):
        sys.exit()
