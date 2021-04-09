from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from app.setting import settings

class paramWindow(QWidget):
    def __init__(self, screen):
        super().__init__()

        self.move(int(screen[0] * 0.5) - self.rect().center().x(), int(screen[1] * 0.5) - self.rect().center().y())
        self.init_ui()
        self.signal_connect()
        #self.setStyleSheet("background-color: #33343b; color: #AAAAAA")
        #self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("preferences")

    def init_ui(self):

        ##############################################################
                                #Layout#
        ##############################################################

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        ##############################################################
                                #Label#
        ##############################################################

        self.label = QLabel("test")
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setStyleSheet('color: red')

        ##############################################################
                                #Button#
        ##############################################################

        self.buttonConclude = QDialogButtonBox()
        self.buttonConclude.addButton('Save', 0)
        self.buttonConclude.addButton('Cancel', 1)

        ##############################################################
                                #Form#
        ##############################################################

        setting = settings()
        formLayout = QFormLayout()
        for path, alias, value in setting.getValue():
            inputText = QLineEdit()
            inputText.setObjectName(path)
            inputText.setText(value)
            formLayout.addRow(alias, inputText)

        ##############################################################
                                #Add Layout#
        ##############################################################

        layout.addWidget(self.label)
        layout.addLayout(formLayout)
        layout.addWidget(self.buttonConclude)
        self.setLayout(layout)


    def signal_connect(self):
        self.buttonConclude.accepted.connect(self.save)
        self.buttonConclude.rejected.connect(self.cancel)

    def save(self):
        print('nice')

        tmp = self.findChild(QLineEdit, "link/yts")
        print(tmp.text())
    
    def cancel(self):
        print('cancel')
        self.close()