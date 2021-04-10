from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDialogButtonBox, QHBoxLayout, QLineEdit, QSlider, QWidget
from app.setting import settings
from gui.widgets import sliderInd, textInput

class paramWindow(QWidget):
    def __init__(self, screen):
        super().__init__()

        self.move(int(screen[0] * 0.5) - self.rect().center().x(), int(screen[1] * 0.5) - self.rect().center().y())
        self.setMinimumWidth(800)
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

        self.setting = settings()
        vLayout = QVBoxLayout()

        for param in self.setting.getValue():
            if param['input_type'] == 'text':
                setting = textInput(param['value'], param['path'], param['alias'])
            elif param['input_type'] == 'slider':
                setting = sliderInd(value=param['value'],path=param['path'], alias=param['alias'])

            vLayout.addLayout(setting)
        ##############################################################
                                #Add Layout#
        ##############################################################

        layout.addWidget(self.label)
        layout.addLayout(vLayout)
        layout.addWidget(self.buttonConclude)
        self.setLayout(layout)


    def signal_connect(self):
        self.buttonConclude.accepted.connect(self.save)
        self.buttonConclude.rejected.connect(self.cancel)

    def save(self):
        for param in self.children():
            if type(param) == QLineEdit:
                self.setting.setValue(param.objectName(), param.text())
            elif type(param) == QSlider:
                self.setting.setValue(param.objectName(), param.value())

        self.setting.sync()
    
    def cancel(self):

        self.close()