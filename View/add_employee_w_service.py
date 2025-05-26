import bcrypt
from Service.db_service import DatabaseService
from Data.User_Data import *

class AddEmployeeService:
    def add_employee(
        self, first_name, last_name, surname, phone_number, birthday, 
        passport, place_of_registration, place_of_residence, family, 
        conscription, education, login, password, role
    ):
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