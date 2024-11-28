from PyQt6 import QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Service.user_service import *
from View_win.user_info_window import UserInfoWindow  


def open_user_info_window(self):
    self.user_info_window = UserInfoWindow()
    self.user_info_window.show()
    self.close()


def get_auth(self):
    login = self.lineEdit.text().strip()
    password = self.lineEdit_2.text().strip()
    result = User_Service().fill_user(login, password)

    if result == "":
        user = User_Service().authorised_user
        if user.Role == User_Role.EMPLOYEE:
            open_user_info_window(self)
        elif user.Role == User_Role.BOSS:
            open_user_info_window(self)
        elif user.Role == User_Role.HR_DEPARTMENT:
            print(f"Отдел кадров {user.full_name}")
    else:
       QMessageBox.critical(self, "Ошибка", result)