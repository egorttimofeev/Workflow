from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.db_connector import get_user_info

class Ui_UserInfoWindow(object):
    def setupUi(self, UserInfoWindow, login):
        UserInfoWindow.setObjectName("UserInfoWindow")
        UserInfoWindow.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(UserInfoWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_first_name = QtWidgets.QLabel(self.centralwidget)
        self.label_first_name.setGeometry(QtCore.QRect(20, 40, 290, 30))
        self.label_first_name.setObjectName("label_first_name")

        self.label_last_name = QtWidgets.QLabel(self.centralwidget)
        self.label_last_name.setGeometry(QtCore.QRect(20, 80, 290, 30))
        self.label_last_name.setObjectName("label_last_name")

        self.label_surname = QtWidgets.QLabel(self.centralwidget)
        self.label_surname.setGeometry(QtCore.QRect(20, 120, 290, 30))
        self.label_surname.setObjectName("label_surname")

        self.label_role = QtWidgets.QLabel(self.centralwidget)
        self.label_role.setGeometry(QtCore.QRect(20, 160, 290, 30))
        self.label_role.setObjectName("label_role")

        self.label_phone_number = QtWidgets.QLabel(self.centralwidget)
        self.label_phone_number.setGeometry(QtCore.QRect(20, 200, 290, 30))
        self.label_phone_number.setObjectName("label_phone_number")

        self.label_birthday = QtWidgets.QLabel(self.centralwidget)
        self.label_birthday.setGeometry(QtCore.QRect(20, 240, 290, 30))
        self.label_birthday.setObjectName("label_birthday")

        self.label_family = QtWidgets.QLabel(self.centralwidget)
        self.label_family.setGeometry(QtCore.QRect(20, 280, 290, 30))
        self.label_family.setObjectName("label_family")

        self.label_conscription = QtWidgets.QLabel(self.centralwidget)
        self.label_conscription.setGeometry(QtCore.QRect(20, 320, 290, 30))
        self.label_conscription.setObjectName("label_conscription")

        self.label_education = QtWidgets.QLabel(self.centralwidget)
        self.label_education.setGeometry(QtCore.QRect(20, 360, 290, 30))
        self.label_education.setObjectName("label_education")

        self.label_passport = QtWidgets.QLabel(self.centralwidget)
        self.label_passport.setGeometry(QtCore.QRect(350, 40, 290, 30))
        self.label_passport.setObjectName("label_passport")

        self.label_place_of_registration = QtWidgets.QLabel(self.centralwidget)
        self.label_place_of_registration.setGeometry(QtCore.QRect(350, 80, 300, 30))
        self.label_place_of_registration.setObjectName("label_place_of_registration")

        self.label_place_of_residence = QtWidgets.QLabel(self.centralwidget)
        self.label_place_of_residence.setGeometry(QtCore.QRect(350, 120, 300, 30))
        self.label_place_of_residence.setObjectName("label_place_of_residence")

        self.button_tabel = QtWidgets.QPushButton("Табель учета", self.centralwidget)
        self.button_tabel.setGeometry(QtCore.QRect(510, 50, 141, 32))
        self.button_tabel.setObjectName("button_tabel")
        self.button_tabel.clicked.connect(lambda: self.open_window(login, 'admin'))

        self.button_add_activity = QtWidgets.QPushButton("Добавить занятия", self.centralwidget)
        self.button_add_activity.setGeometry(QtCore.QRect(510, 10, 141, 32))
        self.button_add_activity.setObjectName("button_add_activity")
        self.button_add_activity.clicked.connect(lambda: self.open_window(login, 'employee'))

        UserInfoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UserInfoWindow)
        self.statusbar.setObjectName("statusbar")
        UserInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UserInfoWindow, login)
        QtCore.QMetaObject.connectSlotsByName(UserInfoWindow)

    def retranslateUi(self, UserInfoWindow, login):
        _translate = QtCore.QCoreApplication.translate
        UserInfoWindow.setWindowTitle(_translate("UserInfoWindow", "Личный кабинет"))

        user_info = get_user_info(login)
        if user_info:
            self.label_first_name.setText(_translate("UserInfoWindow", f"Имя: {user_info['FirstName']}"))
            self.label_last_name.setText(_translate("UserInfoWindow", f"Фамилия: {user_info['LastName']}"))
            self.label_surname.setText(_translate("UserInfoWindow", f"Отчество: {user_info['Surname']}"))
            self.label_role.setText(_translate("UserInfoWindow", f"Роль: {user_info['Role']}"))
            self.label_phone_number.setText(_translate("UserInfoWindow", f"Телефон: {user_info['Phone_number']}"))
            self.label_birthday.setText(_translate("UserInfoWindow", f"День рождения: {user_info['Birthday']}"))
            self.label_family.setText(_translate("UserInfoWindow", f"Семейное положение: {user_info['Family']}"))
            self.label_conscription.setText(_translate("UserInfoWindow", f"Воинская обязанность: {user_info['Conscription']}"))
            self.label_education.setText(_translate("UserInfoWindow", f"Образование: {user_info['Education']}"))
            self.label_passport.setText(_translate("UserInfoWindow", f"Паспорт: {user_info['Passport']}"))
            self.label_place_of_registration.setText(_translate("UserInfoWindow", f"Прописка: {user_info['Place_of_registration']}"))
            self.label_place_of_residence.setText(_translate("UserInfoWindow", f"Проживание: {user_info['Place_of_residence']}"))

            if user_info['Role'] != 'Администратор':
                self.button_tabel.hide()
        else:
            self.label_first_name.setText(_translate("UserInfoWindow", "Имя: Не найдено"))
            self.label_last_name.setText(_translate("UserInfoWindow", "Фамилия: Не найдено"))
            self.label_surname.setText(_translate("UserInfoWindow", "Отчество: Не найдено"))
            self.label_role.setText(_translate("UserInfoWindow", "Роль: Не найдено"))
            self.label_phone_number.setText(_translate("UserInfoWindow", "Телефон: Не найдено"))
            self.label_birthday.setText(_translate("UserInfoWindow", "День рождения: Не найдено"))
            self.label_family.setText(_translate("UserInfoWindow", "Семейное положение: Не найдено"))
            self.label_conscription.setText(_translate("UserInfoWindow", "Воинская обязанность: Не найдено"))
            self.label_education.setText(_translate("UserInfoWindow", "Образование: Не найдено"))
            self.label_passport.setText(_translate("UserInfoWindow", "Паспорт: Не найдено"))
            self.label_place_of_registration.setText(_translate("UserInfoWindow", "Прописка: Не найдено"))
            self.label_place_of_residence.setText(_translate("UserInfoWindow", "Проживание: Не найдено"))

    def open_window(self, login, window_type):
        if window_type == 'admin':
            from View.window_time_sheet import MainWindow as AdminMainWindow
            self.new_window = AdminMainWindow(login)
        elif window_type == 'employee':
            from View.window_activities import MainWindow as EmployeeMainWindow
            self.new_window = EmployeeMainWindow(login)
        self.new_window.show()
        self.close()

class UserInfoWindow(QtWidgets.QMainWindow, Ui_UserInfoWindow):
    def __init__(self, login, parent=None):
        super(UserInfoWindow, self).__init__(parent)
        self.setupUi(self, login)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = "example_login"  # Замените на реальный логин пользователя
    user_info_window = UserInfoWindow(login)
    user_info_window.show()
    sys.exit(app.exec())
