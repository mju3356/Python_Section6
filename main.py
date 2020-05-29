import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
import datetime
import re
from lib.You_Viewer_Layout import Ui_MainWindow

#Form_Class=uic.loadUiType('c:/PythonApp/Section6/ui/You_Viewer_V1.0.ui')[0]

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__=='__main__':
    app=QApplication(sys.argv)
    you_viewer_main=Main()
    you_viewer_main.show()
    app.exec_()
