from PyQt6 import QtCore, QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from View.auth_w_service import *   

class Auth_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.Auth_Ui()

    def Auth_Ui(self):
        self.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel("Введите логин и пароль", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 60, 150, 16))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel("Логин:", self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(214, 140, 51, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel("Пароль:", self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 180, 51, 16))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 140, 151, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 180, 151, 21))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_2 = QtWidgets.QPushButton("Войти", self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 280, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: get_auth(self))

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Auth_Window", "Авторизация"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Auth_Window()
    window.show()
    sys.exit(app.exec())