from PyQt6 import QtCore, QtWidgets
import sys
from auth_w_service import *

class AuthWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AuthWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self):
        AuthWindow.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(AuthWindow)
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
        self.pushButton_2.clicked.connect(lambda: authorize(self))

        AuthWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AuthWindow)
        self.statusbar.setObjectName("statusbar")
        AuthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "Авторизация"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = AuthWindow()
    main_window.show()
    sys.exit(app.exec())