from PyQt6 import QtCore, QtWidgets
import sys
import os
import bcrypt
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Service.user_service import UserService, UserRole
from View.time_sheet_window import TimeSheet
from View.activities_window import ActivitiesWindow
from Service.db_service import DatabaseService
from View.all_workers_window import *
from View.change_password_dialog import ChangePasswordDialog  # Импортируем новый класс

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
    
    def open_change_password_dialog(self):
        dialog = ChangePasswordDialog(self.ui)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            old_password, new_password = dialog.get_passwords()
            self.change_password(old_password, new_password)
    
    def change_password(self, old_password, new_password):
        # Проверяем корректность входных данных
        if not old_password or not new_password:
            QtWidgets.QMessageBox.critical(self.ui, "Ошибка", "Пароли не могут быть пустыми!")
            return
            
        user = UserService().authorised_user
        
        # Получаем данные пользователя
        db_service = DatabaseService()
        
        try:
            # Получаем информацию о пользователе, включая пароль
            query_result = db_service.get_worker_details(user.id_user)
            if query_result.error or not query_result.result:
                QtWidgets.QMessageBox.critical(self.ui, "Ошибка", "Не удалось получить данные пользователя!")
                return
                
            # Пароль должен находиться под индексом 13
            stored_hash = query_result.result[13]
            
            # Преобразуем хеш в байты, если это строка
            stored_hash_bytes = stored_hash
            if isinstance(stored_hash, str):
                stored_hash_bytes = stored_hash.encode('utf-8')
            
            # Проверяем соответствие пароля хешу
            if not bcrypt.checkpw(old_password.encode('utf-8'), stored_hash_bytes):
                QtWidgets.QMessageBox.critical(self.ui, "Ошибка", "Текущий пароль указан неверно!")
                return
                
            # Хешируем новый пароль
            new_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            
            # Обновляем пароль в БД (сохраняем как строку)
            result = db_service.update_user_password(user.id_user, new_hash.decode('utf-8'))
            
            if result.error:
                QtWidgets.QMessageBox.critical(self.ui, "Ошибка", f"Не удалось изменить пароль: {result.error}")
                return
                
            QtWidgets.QMessageBox.information(self.ui, "Успех", "Пароль успешно изменен!")
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ui, "Ошибка", f"Произошла ошибка: {str(e)}")