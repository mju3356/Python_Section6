import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot,pyqtSignal,QUrl
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
        self.user_id='1234'
        self.user_pw='4567'
        #재생 여부 확인
        self.is_play=False


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
        self.previewButton.clicked.connect(self.load_url)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.webEngineView.loadProgress.connect(self.showProgressBrowerLoding)
        self.fileNavButton.clicked.connect(self.selectDownPath)
        self.calendarWidget.clicked.connect(self.appendDate)

    @pyqtSlot()
    def authCheck(self):
        #dlg=AuthDialog()
        #dlg.exec_()
        #self.user_id=dlg.user_id
        #self.user_pw=dlg.user_pw
        if True:
            self.intiAuthActive()
            self.loginButton.setText('인증완료')
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)
            self.append_log_msg('Login Success')
        else:
            QMessageBox.about(self,'인증오류','ID 또는 PW 인증오류')

    def load_url(self):
        url=self.urlTextEdit.text().strip()
        v=re.compile('^https://www.youtube.com/?')
        if self.is_play:
            self.append_log_msg('Stop Click')
            self.webEngineView.load(QUrl('about:blank'))
            self.previewButton.setText('재생')
            self.is_play=False
            self.urlTextEdit.clear()
            self.urlTextEdit.setFocus()
            self.startButton.setEnabled(False)
            self.streamCombobox.clear()
            self.progressBar_2.set_Value(0)
            self.showStatusMsg('인증 완료')
        else:
            if v.match(url) is not None:
                self.append_log_msg ('Play Click')
                self.webEngineView.load (QUrl(url))
                self.showStatusMsg(url+' 재생 중')
                self.previewButton.setText('중지')
                self.is_play=True
                self.startButton.setEnabled(True)
            else:
                QMessageBox.about(self,'URL 형식오류','Youtube 주소 형식이 아닙니다.')
                self.urlTextEdit.clear()
                self.urlTextEdit.setFocus(True)
    @pyqtSlot(int)
    def showProgressBrowerLoding(self,v):
        self.progressBar.setValue(v)

    @pyqtSlot()
    def selectDownPath(self):
        #파일 선택
        #fname=QFileDialog.getOpenFileName(self)
        #self.pathTextEdit.setText(fname[0])
        #경로 선택
        fpath=QFileDialog.getExistingDirectory(self,'Select Directory')
        self.pathTextEdit.setText(fpath)

    @pyqtSlot()
    def appendDate(self):
        cur_date=self.calendarWidget.selectedDate()
        #년월일print('click date',self.calendarWidget.selectedDate().toString())
        #print(str(cur_date.year())+'-'+str(cur_date.month())+'-'+str(cur_date.day()))
        self.append_log_msg('Calendar Click')



    def append_log_msg(self,act):
        now=datetime.datetime.now()
        notDatetime=now.strftime('%Y-%m-%d %H:%M:%S')
        app_msg=self.user_id+' : '+act+'-('+notDatetime+')'
        print(app_msg)
        self.plainTextEdit.appendPlainText(app_msg)

        #활동 로그 저장
        with open('c:/PythonApp/Section6/log/log.txt','a') as f:
            f.write(app_msg+'\n')






if __name__=='__main__':
    app=QApplication(sys.argv)
    you_viewer_main=Main()
    you_viewer_main.show()
    app.exec_()
