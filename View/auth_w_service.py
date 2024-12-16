from PyQt6 import QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Service.user_service import *
from View.user_info_window import UserInfoWindow

def open_user_info_window(self):
    #окно информации о пользователе
    self.user_info_window = UserInfoWindow()
    self.user_info_window.show()
    self.close()

def get_auth(self):
    #аутентификация пользователя
    login = self.lineEdit.text().strip()
    password = self.lineEdit_2.text().strip()
    result = UserService().fill_user(login, password)

    if result == "":
        user = UserService().authorised_user
        if user.Role == UserRole.EMPLOYEE:
            open_user_info_window(self)
        elif user.Role == UserRole.BOSS:
            open_user_info_window(self)
    else:
        QtWidgets.QMessageBox.critical(self, "Ошибка", result)