import sys
import json
from PyQt5.QtWidgets import QMainWindow, QMenu

from gui.param import paramWindow
#from app import setting

class mainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.paramW = None
        self.screen = [app.primaryScreen().size().width(), app.primaryScreen().size().height()]
        #self.setStyleSheet("background-color: #33343b; color: #AAAAAA")
        self.setWindowTitle("PyPop")
        self.resize(int(self.screen[0] * 0.7), int(self.screen[1] * 0.7))

        self._createMenuBar()
    
    def _createMenuBar(self):
        menuBar = self.menuBar()
        optionMenu = QMenu("&Option", self)
        optionMenu.addAction("parameter", self.openParameter)
        optionMenu.addAction("quit", self.close)
        menuBar.addMenu(optionMenu)

    def openParameter(self):
        if self.paramW is None:
            self.paramW = paramWindow(self.screen)
        self.paramW.show()

    def close(self):
        sys.exit()