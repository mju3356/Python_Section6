import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot,pyqtSignal
import datetime
import re
from lib.You_Viewer_Layout import Ui_MainWindow
from lib.AuthDialog import AuthDialog

#Form_Class=uic.loadUiType('c:/PythonApp/Section6/ui/You_Viewer_V1.0.ui')[0]

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #초기화
        self.setupUi(self)
        #초기잠금
        self.initAuthLock()
        #시그널 초기화
        self.initSignal()
        #로그인 관련 변수 선언
        self.user_id=None
        self.user_pw=None

    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')

    #기본 UI 비활성화
    def intiAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증완료')

    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)

    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)

    @pyqtSlot()
    def authCheck(self):
        dlg=AuthDialog()
        dlg.exec_()
        self.user_id=dlg.user_id
        self.user_pw=dlg.user_pw
        if True:
            self.intiAuthActive()
            self.loginButton.setText('인증완료')
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)
        else:
            QMessageBox.about(self,'인증오류','ID 또는 PW 인증오류')

if __name__=='__main__':
    app=QApplication(sys.argv)
    you_viewer_main=Main()
    you_viewer_main.show()
    app.exec_()
