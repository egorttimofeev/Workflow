import mysql.connector

class Role_Service:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def get_role(self, role_id):
        self.cursor.execute("SELECT * FROM Roles WHERE id_role = %s", (role_id,))
        role = self.cursor.fetchone()
        return role

    def add_role(self, role_name):
        self.cursor.execute("INSERT INTO Roles (Role_name) VALUES (%s)", (role_name,))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()