import sys
from PyQt5.QtWidgets import QApplication
from gui.main import mainWindow

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen = mainWindow(app)
fen.show()

app.exec()