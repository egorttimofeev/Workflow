from PyQt6.QtWidgets import QMessageBox
import bcrypt
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Data.User_Data import *
from Service.db_service import *
from Service.singleton import *

class UserService(metaclass=SingletonMeta):
    __user: User = None

    @property
    def authorised_user(self):
        #возвращает авторизованного пользователя
        return self.__user
    
    def fill_user(self, login, password):
        #заполняет данные пользователя после аутентификации
        data_service = DatabaseService()
        query = data_service.get_user_db(login)
        if query.error is None:
            result = query.result   
            if result:
                hashed_password = result[13]
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    self.__user = User(
                        id_user=result[14],
                        Role=result[0],
                        Last_name=result[1], 
                        First_name=result[2], 
                        Surname=result[3], 
                        Phone_number=result[4], 
                        Birthday=result[5], 
                        Passport=result[6],
                        Place_of_registration=result[7], 
                        Place_of_residence=result[8], 
                        Family=result[9], 
                        Conscription=result[10], 
                        Education=result[11], 
                        Login=result[12], 
                        Password=result[13]
                    )
                else:
                    return "Неверный пароль"
                if self.__user.Role > len(UserRole) or self.__user.Role < 1:
                    self.__user = None
                    return "Неизвестная роль пользователя"
                return ""
            else:
                return "Пользователь не найден"
        else:
            return f"Ошибка подключения к базе данных: {query.error}"