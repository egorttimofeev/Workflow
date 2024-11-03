import mysql.connector

class User_Service:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def get_user(self, user_id):
        self.cursor.execute("SELECT * FROM Users WHERE id_user = %s", (user_id,))
        user = self.cursor.fetchone()
        return user

    def add_user(self, first_name, last_name, surname, login, password, role_id, vacation_id):
        self.cursor.execute("""
            INSERT INTO Users (Furst_name, Last_name, Surname, Login, Password, id_role, id_vacation)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, surname, login, password, role_id, vacation_id))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()