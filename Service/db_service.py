from sqlalchemy import create_engine, text
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Data.query_result_data import *
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.txt'))
db_url = config['database']['db_url']

class Database_Service():
    __engine = create_engine(db_url)

    def get_user_db(self, login):
        try:
            with self.__engine.connect() as conn:
                query = text("""
                    SELECT role, last_name, first_name, surname, phone_number, birthday, passport, place_of_registration, place_of_residence, family, conscription, education, login, password, id_user
                    FROM Users 
                    WHERE login = :login""")
                result = conn.execute(query, {"login": login}).fetchone()
                return Query_Result(result, None)
        except Exception as e:
            return Query_Result(None, e)

    def add_activity_to_db(self, id_user, activity_name, duration, date, is_busy):
        try:
            with self.__engine.begin() as conn:  # Используем транзакцию
                query = text("""
                    INSERT INTO Activities (id_user, activity_name, duration, date, is_busy)
                    VALUES (:id_user, :activity_name, :duration, :date, :is_busy)
                """)
                conn.execute(query, {
                    "id_user": id_user,
                    "activity_name": activity_name,
                    "duration": duration,
                    "date": date,
                    "is_busy": int(is_busy),  # Явное преобразование
                })
            return Query_Result(True, None)
        except Exception as e:
            print(f"Ошибка добавления активности: {e}")  # Логируем ошибку
            return Query_Result(None, e)

    def get_activities_by_date(self, date):
        try:
            with self.__engine.connect() as conn:
                query = text("""
                    SELECT u.id_user, CONCAT(u.first_name, ' ', u.last_name, ' ', u.surname) as full_name, a.duration
                    FROM Activities a
                    JOIN Users u ON a.id_user = u.id_user
                    WHERE a.date = :date
                """)
                result = conn.execute(query, {"date": date}).fetchall()
                return Query_Result(result, None)
        except Exception as e:
            return Query_Result(None, e)

    def get_activities_by_employee_and_date(self, employee_name, date):
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
                return Query_Result(result, None)
        except Exception as e:
            return Query_Result(None, e)