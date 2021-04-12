import os
from PyQt5 import QtCore

class settings(QtCore.QSettings):
    def __init__(self):
        super().__init__('WipCorp', 'PyPop')
        self.getValue()

    #def pictureHeight(self, height = None):
    #    if not height:
    #        if self.value("picture/height"):
    #            height = self.value("picture/height")
    #        else:
    #            height = 100
    #    self.setValue('picture/height', height)
    #    return height

    def previewWidth(self, width = None):
        if not width:
            if self.value("preview/width"):
                width = self.value("preview/width")
            else:
                width = 50
        self.setValue('preview/width', width)
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
        val = {}
        val['link/yts'] = {'alias': 'Lien vers api yts', 'value': self.ytsLink(), 'input_type': 'text'}
        #val.append(['picture/height', 'Height of the picture', self.pictureHeight(), 'slider'])
        val['preview/width'] = {'alias': 'Width of the preview', 'value': self.previewWidth(), 'input_type': 'slider', 'min': 50, 'max': 500}
        return val


#setting = settings()
#setting.getValue()
#setting.sync()