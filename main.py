from Service.Role_Service import Role_Service
from Service.User_Service import User_Service
import mysql.connector

# db_connection.py
import mysql.connector

def main():
    mysql.connector.connect(
        host='localhost:8889',
        user='root',
        password='root',
        database='Курсовой_проект'
    )

if __name__ == "__main__":
    main()