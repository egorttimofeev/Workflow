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

def add_activities_to_db(activities):
    with engine.connect() as conn:
        query = text("""
            INSERT INTO Activities (id_user, activity_name, duration, date, trigger_work, trigger_chill)
            VALUES (:id_user, :activity_name, :duration, :date, :trigger_work, :trigger_chill)
        """)
        for activity in activities:
            conn.execute(query, {
                "id_user": activity["id_user"],
                "activity_name": activity["activity_name"],
                "duration": activity["duration"],
                "date": activity["date"],
                "trigger_work": activity["trigger_work"],
                "trigger_chill": activity["trigger_chill"]
            })

def get_time_sheet(login):
    with engine.connect() as conn:
        query = text("""
            SELECT * FROM Activities WHERE id_user = (SELECT id_user FROM Users WHERE login = :login)
        """)
        result = conn.execute(query, {"login": login})
        return result.fetchall()