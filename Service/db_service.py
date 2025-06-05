from sqlalchemy import create_engine, text
import sys
import os
import configparser
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Data.query_result_data import *
from Data.User_Data import *

#чтение конфигурации базы данных
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.txt'))
db_url = config['database']['db_url']

class DatabaseService:
    __engine = create_engine(db_url)

    def get_user_db(self, login):
        #получение данных пользователя из базы данных по логину
        try:
            with self.__engine.connect() as conn:
                query = text("""
                    SELECT role, last_name, first_name, surname, phone_number, birthday, passport, place_of_registration, place_of_residence, family, conscription, education, login, password, id_user
                    FROM Users 
                    WHERE login = :login
                """)
                result = conn.execute(query, {"login": login}).fetchone()
                return QueryResult(result, None)
        except Exception as e:
            return QueryResult(None, e)

    def add_activity_to_db(self, id_user, activity_name, duration, date, is_busy):
        #добавление активности в базу данных
        try:
            with self.__engine.begin() as conn:
                query = text("""
                    INSERT INTO Activities (id_user, activity_name, duration, date, is_busy)
                    VALUES (:id_user, :activity_name, :duration, :date, :is_busy)
                """)
                conn.execute(query, {
                    "id_user": id_user,
                    "activity_name": activity_name,
                    "duration": duration,
                    "date": date,
                    "is_busy": int(is_busy),
                })
            return QueryResult(True, None)
        except Exception as e:
            print(f"Ошибка добавления активности: {e}")
            return QueryResult(None, e)

    def get_activities_by_date(self, date):
        #получение активностей по дате
        try:
            with self.__engine.connect() as conn:
                query = text("""
                    SELECT u.id_user, CONCAT(u.first_name, ' ', u.last_name, ' ', u.surname) as full_name, a.duration
                    FROM Activities a
                    JOIN Users u ON a.id_user = u.id_user
                    WHERE a.date = :date
                """)
                result = conn.execute(query, {"date": date}).fetchall()
                return QueryResult(result, None)
        except Exception as e:
            return QueryResult(None, e)

    def get_activities_by_employee_and_date(self, employee_name, date):
        #получение активностей сотрудника по имени и дате
        try:
            with self.__engine.connect() as conn:
                query = text("""
                    SELECT a.activity_name, a.duration, a.is_busy
                    FROM Activities a
                    JOIN Users u ON a.id_user = u.id_user
                    WHERE CONCAT(u.first_name, ' ', u.last_name, ' ', u.surname) = :employee_name
                    AND a.date = :date
                """)
                result = conn.execute(query, {"employee_name": employee_name, "date": date}).fetchall()
                return QueryResult(result, None)
        except Exception as e:
            return QueryResult(None, e)
        
    def add_user_to_db(self, first_name, last_name, surname, phone_number, birthday, passport, place_of_registration, place_of_residence, family, conscription, education, login, password, role):
        #добавление пользователя в базу данных
        try:
            with self.__engine.begin() as conn:
                query = text("""
                    INSERT INTO Users (first_name, last_name, surname, phone_number, birthday, passport, place_of_registration, place_of_residence, family, conscription, education, login, password, role)
                    VALUES (:first_name, :last_name, :surname, :phone_number, :birthday, :passport, :place_of_registration, :place_of_residence, :family, :conscription, :education, :login, :password, :role)
                """)
                conn.execute(query, {
                    "first_name": first_name,
                    "last_name": last_name,
                    "surname": surname,
                    "phone_number": phone_number,
                    "birthday": birthday,
                    "passport": passport,
                    "place_of_registration": place_of_registration,
                    "place_of_residence": place_of_residence,
                    "family": family,
                    "conscription": conscription,
                    "education": education,
                    "login": login,
                    "password": password,
                    "role": role
                })
            return QueryResult(True, None)
        except Exception as e:
            print(f"Ошибка добавления пользователя: {e}")
            return QueryResult(None, e)
        
    def get_all_workers(self):
        #получение списка всех сотрудников
        try:
            with self.__engine.connect() as conn:
                query = text("""
                    SELECT CONCAT(first_name, ' ', last_name, ' ', surname) as full_name, id_user
                    FROM Users
                """)
                result = conn.execute(query).fetchall()
                return QueryResult(result, None)
        except Exception as e:
            return QueryResult(None, e)

    def get_worker_details(self, worker_id):
        try:
            with self.__engine.connect() as conn:
                query = text("""
                    SELECT first_name, last_name, surname, phone_number, birthday, passport, 
                           place_of_registration, place_of_residence, role, family, 
                           conscription, education, login, password
                    FROM Users
                    WHERE id_user = :worker_id
                """)
                result = conn.execute(query, {"worker_id": worker_id}).fetchone()
                return QueryResult(result, None)
        except Exception as e:
            print(f"Ошибка получения деталей работника: {e}")
            return QueryResult(None, e)

    def delete_worker(self, worker_id):
        #удаление сотрудника по ID
        try:
            with self.__engine.begin() as conn:
                query = text("""
                    DELETE FROM Users
                    WHERE id_user = :worker_id
                """)
                conn.execute(query, {"worker_id": worker_id})
            return QueryResult(True, None)
        except Exception as e:
            return QueryResult(None, e)
        
    def get_workers_count(self):
        try:
            with self.__engine.connect() as conn:
                query = text("SELECT COUNT(*) FROM Users")
                result = conn.execute(query).scalar()
                return QueryResult(result, None)
        except Exception as e:
            return QueryResult(None, e)

    def update_user_password(self, user_id, hashed_password):
        try:
            with self.__engine.begin() as conn:
                query = text("""
                    UPDATE Users 
                    SET password = :password
                    WHERE id_user = :user_id
                """)
                conn.execute(query, {
                    "password": hashed_password,
                    "user_id": user_id
                })
            return QueryResult(True, None)
        except Exception as e:
            print(f"Ошибка обновления пароля: {e}")
            return QueryResult(None, e)
        
    def check_login_exists(self, login):
        try:
            with self.__engine.connect() as conn:
                query = text("""
                    SELECT COUNT(*) FROM Users WHERE login = :login
                """)
                result = conn.execute(query, {"login": login}).scalar()
                return QueryResult(result > 0, None)
        except Exception as e:
            print(f"Ошибка: {e}")
            return QueryResult(None, e)