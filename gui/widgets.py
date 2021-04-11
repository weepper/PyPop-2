from PyQt5.QtWidgets import QSlider, QLabel, QSizePolicy, QHBoxLayout, QLineEdit, QLayout, QWidget
from PyQt5.QtCore import QPoint, QRect, QSize, Qt

class sliderInd(QHBoxLayout):
    def __init__(self, min = 0, max = 100, value = 0, path = '', alias = ''):
        super().__init__()

        #display alias
        self.ali = QLabel(str(alias))
        self.ali.setMinimumWidth(200)

        #display slider
        self.inp = QSlider(Qt.Horizontal)
        self.inp.setMinimum(int(min))
        self.inp.setMaximum(int(max))
        self.inp.setValue(int(value))
        self.inp.setObjectName(path)

        #display value
        self.ind = QLabel(str(value))
        self.ind.setObjectName(path + 'Ind')
        self.addWidget(self.ali)
        self.addWidget(self.inp)
        self.addWidget(self.ind)

        #connect
        self.inp.valueChanged.connect(self.valueChanged)
    
    def valueChanged(self):
        self.ind.setText(str(self.inp.value()))

class textInput(QHBoxLayout):
    def __init__(self, value = 0, path = '', alias = ''):
        super().__init__()

        #display alias
        self.ali = QLabel(str(alias))
        self.ali.setMinimumWidth(200)

        #display slider
        self.inp = QLineEdit()
        self.inp.setText(str(value))
        self.inp.setObjectName(path)

        self.addWidget(self.ali)
        self.addWidget(self.inp)

class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margin, _, _, _ = self.getContentsMargins()

        size += QSize(2 * margin, 2 * margin)
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()

    def asWidget(self):
        widget = QWidget()
        widget.setLayout(self)
        return widget