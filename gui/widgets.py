from PyQt5.QtWidgets import QSlider, QLabel, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

class sliderInd(QHBoxLayout):
    def __init__(self, min = 0, max = 100, value = 0, path = '', alias = ''):
        super().__init__()

        #display alias
        self.ali = QLabel(str(alias))
        #self.ali = QLabel("<font color=#33343b>" + str(alias) + "</font>")
        self.ali.setMinimumWidth(200)

        #display slider
        self.inp = QSlider(Qt.Horizontal)
        self.inp.setMinimum(int(min))
        self.inp.setMaximum(int(max))
        self.inp.setValue(int(value))
        self.inp.setObjectName(path)

        #display value
        self.ind = QLabel("<font color=#33343b>" + str(value) + "</font>")
        self.ind.setObjectName(path + 'Ind')
        self.addWidget(self.ali)
        self.addWidget(self.inp)
        self.addWidget(self.ind)

        #connect
        self.inp.valueChanged.connect(self.valueChanged)
    
    def valueChanged(self):
        self.ind.setText("<font color=#33343b>" + str(self.inp.value()) + "</font>")

class textInput(QHBoxLayout):
    def __init__(self, value = 0, path = '', alias = ''):
        super().__init__()

        #display alias
        self.ali = QLabel("<font color=#33343b>" + str(alias) + "</font>")
        self.ali.setMinimumWidth(200)

        #display slider
        self.inp = QLineEdit()
        self.inp.setText(str(value))
        self.inp.setObjectName(path)

        self.addWidget(self.ali)
        self.addWidget(self.inp)