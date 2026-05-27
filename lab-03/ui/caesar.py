import os
import sys
import requests  # Thư viện để gọi API gửi lên server Flask
from PyQt5 import QtCore, QtGui, QtWidgets

# Cấu hình sửa lỗi hiển thị nền tảng và co rúm chữ
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 350)  # Thu gọn kích thước cửa sổ chính cho vừa vặn, đẹp mắt
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Tiêu đề CAESAR CIPHER
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # Nhãn PlainText
        self.Lable1 = QtWidgets.QLabel(self.centralwidget)
        self.Lable1.setGeometry(QtCore.QRect(40, 80, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lable1.setFont(font)
        self.Lable1.setObjectName("Lable1")
        
        # Nhãn Key
        self.Lable2 = QtWidgets.QLabel(self.centralwidget)
        self.Lable2.setGeometry(QtCore.QRect(40, 130, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lable2.setFont(font)
        self.Lable2.setObjectName("Lable2")
        
        # Nhãn CipherText
        self.lable2 = QtWidgets.QLabel(self.centralwidget)
        self.lable2.setGeometry(QtCore.QRect(40, 180, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lable2.setFont(font)
        self.lable2.setObjectName("lable2")
        
        # Ô nhập Key
        self.txtKey = QtWidgets.QLineEdit(self.centralwidget)
        self.txtKey.setGeometry(QtCore.QRect(140, 130, 240, 25))
        self.txtKey.setObjectName("txtKey")
        
        # Ô nhập PlainText (Đổi từ QTextEdit sang QLineEdit cho đồng bộ, lấy text dễ hơn)
        self.txtPlain = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPlain.setGeometry(QtCore.QRect(140, 80, 240, 25))
        self.txtPlain.setObjectName("txtPlain")
        
        # Ô hiển thị CipherText
        self.txtCipher = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCipher.setGeometry(QtCore.QRect(140, 180, 240, 25))
        self.txtCipher.setObjectName("txtCipher")
        
        # Nút Encrypt (Đã sửa lại kích thước 90x30 cho nút to rõ chữ)
        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(140, 240, 90, 30))
        self.btnEncrypt.setObjectName("btnEncrypt")
        
        # Nút Decrypt (Đã sửa lại kích thước 90x30 cho nút to rõ chữ)
        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(290, 240, 90, 30))
        self.btnDecrypt.setObjectName("btnDecrypt")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # ================= KẾT NỐI SỰ KIỆN NÚT BẤM =================
        self.btnEncrypt.clicked.connect(self.handle_encrypt)
        self.btnDecrypt.clicked.connect(self.handle_decrypt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caesar Cipher Tool"))
        self.label.setText(_translate("MainWindow", "CAESAR CIPHER"))
        self.Lable1.setText(_translate("MainWindow", "PlainText:"))
        self.Lable2.setText(_translate("MainWindow", "Key:"))
        self.lable2.setText(_translate("MainWindow", "CipherText:"))
        self.btnEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt"))

    # ================= HÀM XỬ LÝ GỌI API MÃ HÓA =================
    def handle_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        plain_text = self.txtPlain.text()
        key_text = self.txtKey.text()
        
        if not plain_text or not key_text:
            self.txtCipher.setText("Lỗi: Thiếu PlainText hoặc Key!")
            return
            
        try:
            payload = {"plain_text": plain_text, "key": int(key_text)}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                result = response.json()
                self.txtCipher.setText(result.get("encrypted_text", ""))
            else:
                self.txtCipher.setText("Lỗi kết nối Server!")
        except Exception as e:
            self.txtCipher.setText(f"Lỗi: {str(e)}")

    # ================= HÀM XỬ LÝ GỌI API GIẢI MÃ =================
    def handle_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        cipher_text = self.txtCipher.text()
        key_text = self.txtKey.text()
        
        if not cipher_text or not key_text:
            self.txtPlain.setText("Lỗi: Thiếu CipherText hoặc Key!")
            return
            
        try:
            payload = {"cipher_text": cipher_text, "key": int(key_text)}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                result = response.json()
                self.txtPlain.setText(result.get("decrypted_text", ""))
            else:
                self.txtPlain.setText("Lỗi kết nối Server!")
        except Exception as e:
            self.txtPlain.setText(f"Lỗi: {str(e)}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())