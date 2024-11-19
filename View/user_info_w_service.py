from PyQt6 import QtCore
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.db_connector import get_user_info

def retranslateUi(self, UserInfoWindow, login):
    _translate = QtCore.QCoreApplication.translate
    UserInfoWindow.setWindowTitle(_translate("UserInfoWindow", "Личный кабинет"))

    user_info = get_user_info(login)
    if user_info:
        self.label_first_name.setText(_translate("UserInfoWindow", f"Имя: {user_info['FirstName']}"))
        self.label_last_name.setText(_translate("UserInfoWindow", f"Фамилия: {user_info['LastName']}"))
        self.label_surname.setText(_translate("UserInfoWindow", f"Отчество: {user_info['Surname']}"))
        self.label_role.setText(_translate("UserInfoWindow", f"Роль: {user_info['Role']}"))
        self.label_phone_number.setText(_translate("UserInfoWindow", f"Телефон: {user_info['Phone_number']}"))
        self.label_birthday.setText(_translate("UserInfoWindow", f"День рождения: {user_info['Birthday']}"))
        self.label_family.setText(_translate("UserInfoWindow", f"Семейное положение: {user_info['Family']}"))
        self.label_conscription.setText(_translate("UserInfoWindow", f"Воинская обязанность: {user_info['Conscription']}"))
        self.label_education.setText(_translate("UserInfoWindow", f"Образование: {user_info['Education']}"))
        self.label_passport.setText(_translate("UserInfoWindow", f"Паспорт: {user_info['Passport']}"))
        self.label_place_of_registration.setText(_translate("UserInfoWindow", f"Прописка: {user_info['Place_of_registration']}"))
        self.label_place_of_residence.setText(_translate("UserInfoWindow", f"Проживание: {user_info['Place_of_residence']}"))

        if user_info['Role'] != 'Администратор':
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

def open_window(self, login, window_type):
    if window_type == 'admin':
        from View.time_sheet_window import MainWindow as AdminMainWindow
        self.new_window = AdminMainWindow(login)
    elif window_type == 'employee':
        from View.activities_window import MainWindow as EmployeeMainWindow
        self.new_window = EmployeeMainWindow(login)
    self.new_window.show()
    self.centralwidget.window().close()