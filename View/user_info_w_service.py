from PyQt6 import QtCore
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Service.user_service import UserService, UserRole
from View.time_sheet_window import TimeSheet
from View.activities_window import ActivitiesWindow
from View.all_workers_window import *

class UserInfoService:
    def __init__(self, ui):
        self.ui = ui

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.setWindowTitle(_translate("UserInfoWindow", "Личный кабинет"))

        #получение авторизованного пользователя
        self.user = UserService().authorised_user

        #роль пользователя
        role_name = {
            1: "Сотрудник",
            2: "Начальник",
        }.get(self.user.Role, "Неизвестная роль")

        #полное имя пользователя
        full_name = f"{self.user.First_name} {self.user.Last_name} {self.user.Surname}"

        #текст меток с информацией о пользователе
        self.ui.label_full_name.setText(_translate("UserInfoWindow", f"{full_name}"))
        self.ui.label_role.setText(_translate("UserInfoWindow", f"Роль: {role_name}"))
        self.ui.label_phone_number.setText(_translate("UserInfoWindow", f"Телефон: {self.user.Phone_number}"))
        self.ui.label_birthday.setText(_translate("UserInfoWindow", f"День рождения: {self.user.Birthday}"))
        self.ui.label_family.setText(_translate("UserInfoWindow", f"Семейное положение: {self.user.Family}"))
        self.ui.label_conscription.setText(_translate("UserInfoWindow", f"Воинская обязанность: {self.user.Conscription}"))
        self.ui.label_education.setText(_translate("UserInfoWindow", f"Образование: {self.user.Education}"))
        self.ui.label_passport.setText(_translate("UserInfoWindow", f"Паспорт: {self.user.Passport}"))
        self.ui.label_place_of_registration.setText(_translate("UserInfoWindow", f"Прописка: {self.user.Place_of_registration}"))
        self.ui.label_place_of_residence.setText(_translate("UserInfoWindow", f"Проживание: {self.user.Place_of_residence}"))

        #скрываем кнопки для сотрудников
        if self.user.Role == UserRole.EMPLOYEE:
            self.ui.button_tabel.hide()
            self.ui.button_all_workers.hide()

    def open_time_sheet_window(self):
        user_service = UserService()
        current_user = user_service.authorised_user
        if current_user:
            self.time_sheet_window = TimeSheet(current_user.Login)
            self.time_sheet_window.show()
            self.ui.close()

    def open_activities_window(self):
        self.activities_window = ActivitiesWindow()
        self.activities_window.show()
        self.ui.close()

    def closeEvent(self, event):
        self.service.on_worker_details_close()
        event.accept()
    
    def open_all_workers_window(self):
        self.all_workers_window = AllWorkersWindow()
        self.all_workers_window.show()