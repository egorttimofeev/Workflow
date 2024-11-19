from PyQt6 import QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.db_connector import get_auth_user

def authorize(self):
    login = self.lineEdit.text()
    password = self.lineEdit_2.text()
    auth_info = get_auth_user(login, password)
    if auth_info:
        open_user_info_window(self, login)
    else:
        QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", "Неверный логин или пароль")

def open_user_info_window(self, login):
    from View.user_info_window import UserInfoWindow  
    self.user_info_window = UserInfoWindow(login)
    self.user_info_window.show()
    self.centralwidget.window().close()