from PyQt6 import QtCore, QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.db_connector import get_auth_user


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel("Войдите в систему", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 60, 131, 16))
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
        self.pushButton_2.clicked.connect(self.authorize)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "Authorize"))

    def authorize(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        auth_info = get_auth_user(login, password)
        if auth_info:
            self.open_user_info_window(login)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Ошибка", "Неверный логин или пароль")

    def open_user_info_window(self, login):
        from user_info import UserInfoWindow  # Импортируем здесь, чтобы избежать циклического импорта
        self.user_info_window = UserInfoWindow(login)
        self.user_info_window.show()
        self.centralwidget.window().close()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())