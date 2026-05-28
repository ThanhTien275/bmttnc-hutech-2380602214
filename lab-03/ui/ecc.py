


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtInfor = QtWidgets.QTextEdit(self.centralwidget)
        self.txtInfor.setGeometry(QtCore.QRect(110, 90, 221, 64))
        self.txtInfor.setObjectName("txtInfor")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtSignature = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSignature.setGeometry(QtCore.QRect(110, 200, 221, 64))
        self.txtSignature.setObjectName("txtSignature")
        self.btnGenerateKeys = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerateKeys.setGeometry(QtCore.QRect(280, 60, 91, 17))
        self.btnGenerateKeys.setObjectName("btnGenerateKeys")
        self.btnSign = QtWidgets.QPushButton(self.centralwidget)
        self.btnSign.setGeometry(QtCore.QRect(100, 290, 56, 17))
        self.btnSign.setObjectName("btnSign")
        self.btnVerify = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerify.setGeometry(QtCore.QRect(250, 290, 56, 17))
        self.btnVerify.setObjectName("btnVerify")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ECC CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Information"))
        self.label_3.setText(_translate("MainWindow", "Signature"))
        self.btnGenerateKeys.setText(_translate("MainWindow", "Generate Keys"))
        self.btnSign.setText(_translate("MainWindow", "Sign"))
        self.btnVerify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
