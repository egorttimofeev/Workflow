from PyQt6 import QtCore, QtWidgets
import sys
from user_info_w_service import *

class UserInfoWindow(QtWidgets.QMainWindow):
    def __init__(self, login, parent=None):
        super(UserInfoWindow, self).__init__(parent)
        self.setupUi(self, login)
        
    def setupUi(self, UserInfoWindow, login):
        UserInfoWindow.setObjectName("UserInfoWindow")
        UserInfoWindow.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(UserInfoWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_first_name = QtWidgets.QLabel(self.centralwidget)
        self.label_first_name.setGeometry(QtCore.QRect(20, 40, 290, 30))
        self.label_first_name.setObjectName("label_first_name")

        self.label_last_name = QtWidgets.QLabel(self.centralwidget)
        self.label_last_name.setGeometry(QtCore.QRect(20, 80, 290, 30))
        self.label_last_name.setObjectName("label_last_name")

        self.label_surname = QtWidgets.QLabel(self.centralwidget)
        self.label_surname.setGeometry(QtCore.QRect(20, 120, 290, 30))
        self.label_surname.setObjectName("label_surname")

        self.label_role = QtWidgets.QLabel(self.centralwidget)
        self.label_role.setGeometry(QtCore.QRect(20, 160, 290, 30))
        self.label_role.setObjectName("label_role")

        self.label_phone_number = QtWidgets.QLabel(self.centralwidget)
        self.label_phone_number.setGeometry(QtCore.QRect(20, 200, 290, 30))
        self.label_phone_number.setObjectName("label_phone_number")

        self.label_birthday = QtWidgets.QLabel(self.centralwidget)
        self.label_birthday.setGeometry(QtCore.QRect(20, 240, 290, 30))
        self.label_birthday.setObjectName("label_birthday")

        self.label_family = QtWidgets.QLabel(self.centralwidget)
        self.label_family.setGeometry(QtCore.QRect(20, 280, 290, 30))
        self.label_family.setObjectName("label_family")

        self.label_conscription = QtWidgets.QLabel(self.centralwidget)
        self.label_conscription.setGeometry(QtCore.QRect(20, 320, 290, 30))
        self.label_conscription.setObjectName("label_conscription")

        self.label_education = QtWidgets.QLabel(self.centralwidget)
        self.label_education.setGeometry(QtCore.QRect(20, 360, 290, 30))
        self.label_education.setObjectName("label_education")

        self.label_passport = QtWidgets.QLabel(self.centralwidget)
        self.label_passport.setGeometry(QtCore.QRect(350, 40, 290, 30))
        self.label_passport.setObjectName("label_passport")

        self.label_place_of_registration = QtWidgets.QLabel(self.centralwidget)
        self.label_place_of_registration.setGeometry(QtCore.QRect(350, 80, 300, 30))
        self.label_place_of_registration.setObjectName("label_place_of_registration")

        self.label_place_of_residence = QtWidgets.QLabel(self.centralwidget)
        self.label_place_of_residence.setGeometry(QtCore.QRect(350, 120, 300, 30))
        self.label_place_of_residence.setObjectName("label_place_of_residence")

        self.button_tabel = QtWidgets.QPushButton("Табель учета", self.centralwidget)
        self.button_tabel.setGeometry(QtCore.QRect(510, 50, 141, 32))
        self.button_tabel.setObjectName("button_tabel")
        self.button_tabel.clicked.connect(lambda: open_window(self, login, 'admin'))

        self.button_add_activity = QtWidgets.QPushButton("Добавить занятия", self.centralwidget)
        self.button_add_activity.setGeometry(QtCore.QRect(510, 10, 141, 32))
        self.button_add_activity.setObjectName("button_add_activity")
        self.button_add_activity.clicked.connect(lambda: open_window(self, login, 'employee'))

        UserInfoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UserInfoWindow)
        self.statusbar.setObjectName("statusbar")
        UserInfoWindow.setStatusBar(self.statusbar)

        retranslateUi(self, UserInfoWindow, login)
        QtCore.QMetaObject.connectSlotsByName(UserInfoWindow)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = "example_login"  # Замените на реальный логин пользователя
    user_info_window = UserInfoWindow(login)
    user_info_window.show()
    sys.exit(app.exec())