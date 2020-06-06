from PyQt5.QtCore import QObject,pyqtSignal,pyqtSlot
from PyQt5.QtMultimedia import QSound

class IntroWorker(QObject):
     StartMsg=pyqtSignal(str,str)
     @pyqtSlot()
     def PlayBGM(self):
         self.intro=QSound('c:/PythonApp/Section6/resource/intro.wav')
         self.intro.play()
         self.StartMsg.emit('Ananymous',self.intro.fileName())
