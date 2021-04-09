import os
from PyQt5 import QtCore

class settings(QtCore.QSettings):
    def __init__(self):
        super().__init__('WipCorp', 'PyPop')
        self.getValue()

    def pictureHeight(self, height = None):
        if not height:
            if self.value("picture/height"):
                height = self.value("picture/height")
            else:
                height = 100
        self.setValue('picture/height', height)
        return height

    def pictureWidth(self, width = None):
        if not width:
            if self.value("picture/width"):
                width = self.value("picture/width")
            else:
                width = 50
        self.setValue('picture/width', width)
        return width

    def ytsLink(self, link = None):
        if not link:
            if self.value("link/yts"):
                link = self.value("link/yts")
            else:
                link = "https://yts.mx/api/v2"
        self.setValue('link/yts', link)
        return link
    
    def getValue(self):
        val = []
        val.append(['link/yts', 'Lien vers api yts', self.ytsLink()])
        val.append(['picture/height', 'Height of the picture', self.pictureHeight()])
        val.append(['picture/width', 'Width of the picture', self.pictureWidth()])
        return val


#setting = settings()
#setting.getValue()
#setting.sync()