from PyQt6 import QtCore
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Service.user_service import *

def retranslateUi(self):
    _translate = QtCore.QCoreApplication.translate
    self.setWindowTitle(_translate("UserInfoWindow", "Личный кабинет"))

    self.user = User_Service().authorised_user
    if self.user:
        self.label_first_name.setText(_translate("UserInfoWindow", f"Имя: {self.user.First_name}"))
        self.label_last_name.setText(_translate("UserInfoWindow", f"Фамилия: {self.user.Last_name}"))
        self.label_surname.setText(_translate("UserInfoWindow", f"Отчество: {self.user.Surname}"))
        self.label_role.setText(_translate("UserInfoWindow", f"Роль: {self.user.Role}"))
        self.label_phone_number.setText(_translate("UserInfoWindow", f"Телефон: {self.user.Phone_number}"))
        self.label_birthday.setText(_translate("UserInfoWindow", f"День рождения: {self.user.Birthday}"))
        self.label_family.setText(_translate("UserInfoWindow", f"Семейное положение: {self.user.Family}"))
        self.label_conscription.setText(_translate("UserInfoWindow", f"Воинская обязанность: {self.user.Conscription}"))
        self.label_education.setText(_translate("UserInfoWindow", f"Образование: {self.user.Education}"))
        self.label_passport.setText(_translate("UserInfoWindow", f"Паспорт: {self.user.Passport}"))
        self.label_place_of_registration.setText(_translate("UserInfoWindow", f"Прописка: {self.user.Place_of_registration}"))
        self.label_place_of_residence.setText(_translate("UserInfoWindow", f"Проживание: {self.user.Place_of_residence}"))

        if self.user.Role == User_Role.EMPLOYEE:
            self.button_tabel.hide()
    else:
        self.label_first_name.setText(_translate("UserInfoWindow", "Имя: Не найдено"))
        self.label_last_name.setText(_translate("UserInfoWindow", "Фамилия: Не найдено"))
        self.label_surname.setText(_translate("UserInfoWindow", "Отчество: Не найдено"))
        self.label_role.setText(_translate("UserInfoWindow", "Роль: Не найдено"))
        self.label_phone_number.setText(_translate("UserInfoWindow", "Телефон: Не найдено"))
        self.label_birthday.setText(_translate("UserInfoWindow", "День рождения: Не найдено"))
        self.label_family.setText(_translate("UserInfoWindow", "Семейное положение: Не найдено"))
        self.label_conscription.setText(_translate("UserInfoWindow", "Воинская обязанность: Не найдено"))
        self.label_education.setText(_translate("UserInfoWindow", "Образование: Не найдено"))
        self.label_passport.setText(_translate("UserInfoWindow", "Паспорт: Не найдено"))
        self.label_place_of_registration.setText(_translate("UserInfoWindow", "Прописка: Не найдено"))
        self.label_place_of_residence.setText(_translate("UserInfoWindow", "Проживание: Не найдено"))

def open_window(self, window_type):
    if window_type == User_Role.BOSS:
        from View.View_win.time_sheet_window import MainWindow as AdminMainWindow
        self.new_window = AdminMainWindow()
    elif window_type == User_Role.EMPLOYEE:
        from View.View_win.activities_window import MainWindow as EmployeeMainWindow
        self.new_window = EmployeeMainWindow()
    self.new_window.show()
    self.close()