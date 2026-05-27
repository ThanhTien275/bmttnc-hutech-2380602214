import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# --- CẤU HÌNH FIX LỖI NỀN TẢNG & CO RÚM CHỮ ---
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "./platforms"
from PyQt5 import QtCore
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# Import giao diện từ file caesar.py nằm trong thư mục ui
from ui.caesar import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối sự kiện nút bấm với hàm xử lý
        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        
        # Lấy dữ liệu từ giao diện dựa trên đúng tên biến trong file caesar.py của bạn
        payload = {
    "plain_text": self.ui.txtPlain.text(),  # <-- Sửa ở đây
    "key": int(self.ui.txtKey.text())
}
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Hiển thị kết quả mã hóa lên ô txtCipher
                self.ui.txtCipher.setText(data.get("encrypted_text", data.get("encrypted_message", "")))
                
                # Hiển thị thông báo thành công
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        
        payload = {
    "cipher_text": self.ui.txtCipher.text(),  # <-- Sửa ở đây
    "key": int(self.ui.txtKey.text())
}
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Hiển thị kết quả giải mã lên ô txtPlain
                self.ui.txtPlain.setText(data.get("decrypted_text", data.get("decrypted_message", "")))
                
                # Hiển thị thông báo thành công
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())