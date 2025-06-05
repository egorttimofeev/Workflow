import bcrypt
from Service.db_service import DatabaseService
from Data.User_Data import *
from PyQt6 import QtWidgets

class AddEmployeeService:
    def add_employee(
        self, first_name, last_name, surname, phone_number, birthday, 
        passport, place_of_registration, place_of_residence, family, 
        conscription, education, login, password, role
    ):
        #проверка существования логина
        db_service = DatabaseService()
        login_check = db_service.check_login_exists(login)
        
        if login_check.error:
            #обработка ошибки проверки логина
            print(f"Ошибка: {login_check.error}")
            return False
        
        if login_check.result:
            QtWidgets.QMessageBox.critical(None, "Ошибка", "Пользователь с таким логином уже существует!")
            return False
        
        #проверка формата даты рождения
        try:
            if not birthday or len(birthday.split('-')) != 3:
                QtWidgets.QMessageBox.critical(None, "Ошибка", 
                    "Дата рождения должна быть в формате ГГГГ-ММ-ДД (например, 1990-01-01)")
                return False
        except:
            QtWidgets.QMessageBox.critical(None, "Ошибка", 
                "Дата рождения должна быть в формате ГГГГ-ММ-ДД (например, 1990-01-01)")
            return False
        
        #хеширование пароля
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)

        #добавление пользователя в бд
        db_service = DatabaseService()
        result = db_service.add_user_to_db(
            first_name,
            last_name,
            surname,
            phone_number,
            birthday,
            passport,
            place_of_registration,
            place_of_residence,
            family,
            conscription,
            education,
            login,
            hashed_password.decode('utf-8'),
            role.value
        )
        return result