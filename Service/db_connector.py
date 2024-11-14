from sqlalchemy import create_engine, text
import bcrypt

engine = create_engine('mysql+mysqlconnector://root:root@localhost:8889/curs_project')

def get_auth_user(login, password):
    with engine.connect() as conn:
        query = text("SELECT login, password, role, first_name, last_name FROM Users WHERE login = :login")
        result = conn.execute(query, {"login": login})
        auth_info = result.fetchone()
        
        if auth_info is None:
            return None
        
        hashed_password = auth_info[1]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return auth_info
        else:
            return None

def get_user_info(login):
    with engine.connect() as conn:
        query = text("""
            SELECT first_name, last_name, surname, role, phone_number, birthday, passport, 
                   place_of_registration, place_of_residence, family, conscription, education
            FROM Users
            WHERE login = :login
        """)
        result = conn.execute(query, {"login": login})
        row = result.fetchone()
        if row:
            return {
                "FirstName": row[0],
                "LastName": row[1],
                "Surname": row[2],
                "Role": row[3],
                "Phone_number": row[4],
                "Birthday": row[5],
                "Passport": row[6],
                "Place_of_registration": row[7],
                "Place_of_residence": row[8],
                "Family": row[9],
                "Conscription": row[10],
                "Education": row[11]
            }
        return None

def add_activity_to_db(login, activity_name, duration, date, is_busy):
    with engine.connect() as conn:
        # Добавляем занятие в таблицу Activities
        query = text("""
            INSERT INTO Activities (Activity_name, Duration, trigger_work, trigger_chill)
            VALUES (:activity_name, :duration, :trigger_work, :trigger_chill)
        """)
        result = conn.execute(query, {
            "activity_name": activity_name,
            "duration": duration,
            "trigger_work": is_busy,
            "trigger_chill": not is_busy
        })
        
        # Получаем id добавленного занятия
        activity_id = result.lastrowid
        
        # Добавляем запись в таблицу Work_activities
        query = text("""
            INSERT INTO Work_activities (id_activity, date)
            VALUES (:id_activity, :date)
        """)
        conn.execute(query, {
            "id_activity": activity_id,
            "date": date
        })
