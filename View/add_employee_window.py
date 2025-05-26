from PyQt6 import QtWidgets
from Data.User_Data import UserRole
from View.add_employee_w_service import AddEmployeeService

class AddEmployeeWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить работника")
        self.setGeometry(100, 100, 600, 300)

        #создаем макет
        self.layout = QtWidgets.QGridLayout()

        #настраиваем метки и поля ввода для данных сотрудника

        self.label_first_name = QtWidgets.QLabel("Имя:")
        self.input_first_name = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_first_name, 0, 0)
        self.layout.addWidget(self.input_first_name, 0, 1)

        self.label_last_name = QtWidgets.QLabel("Фамилия:")
        self.input_last_name = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_last_name, 1, 0)
        self.layout.addWidget(self.input_last_name, 1, 1)

        self.label_surname = QtWidgets.QLabel("Отчество:")
        self.input_surname = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_surname, 2, 0)
        self.layout.addWidget(self.input_surname, 2, 1)

        self.label_phone_number = QtWidgets.QLabel("Телефон:")
        self.input_phone_number = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_phone_number, 3, 0)
        self.layout.addWidget(self.input_phone_number, 3, 1)

        self.label_birthday = QtWidgets.QLabel("День рождения:")
        self.input_birthday = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_birthday, 4, 0)
        self.layout.addWidget(self.input_birthday, 4, 1)

        self.label_passport = QtWidgets.QLabel("Паспорт:")
        self.input_passport = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_passport, 5, 0)
        self.layout.addWidget(self.input_passport, 5, 1)

        self.label_place_of_registration = QtWidgets.QLabel("Прописка:")
        self.input_place_of_registration = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_place_of_registration, 6, 0)
        self.layout.addWidget(self.input_place_of_registration, 6, 1)

        self.label_place_of_residence = QtWidgets.QLabel("Проживание:")
        self.input_place_of_residence = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_place_of_residence, 7, 0)
        self.layout.addWidget(self.input_place_of_residence, 7, 1)

        self.label_family = QtWidgets.QLabel("Семейное положение:")
        self.input_family = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_family, 8, 0)
        self.layout.addWidget(self.input_family, 8, 1)

        self.label_conscription = QtWidgets.QLabel("Воинская обязанность:")
        self.input_conscription = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_conscription, 0, 2)
        self.layout.addWidget(self.input_conscription, 0, 3)

        self.label_education = QtWidgets.QLabel("Образование:")
        self.input_education = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_education, 1, 2)
        self.layout.addWidget(self.input_education, 1, 3)

        self.label_login = QtWidgets.QLabel("Логин:")
        self.input_login = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_login, 2, 2)
        self.layout.addWidget(self.input_login, 2, 3)

        self.label_password = QtWidgets.QLabel("Пароль:")
        self.input_password = QtWidgets.QLineEdit()
        self.layout.addWidget(self.label_password, 3, 2)
        self.layout.addWidget(self.input_password, 3, 3)

        self.label_role = QtWidgets.QLabel("Роль:")
        self.combo_role = QtWidgets.QComboBox()
        self.combo_role.addItems(["Сотрудник", "Начальник"])
        self.layout.addWidget(self.label_role, 4, 2)
        self.layout.addWidget(self.combo_role, 4, 3)

        #настраиваем кнопку для добавления сотрудника
        self.button_add = QtWidgets.QPushButton("Добавить")
        self.button_add.setStyleSheet("background-color: lightblue;")
        self.button_add.clicked.connect(self.add_employee)
        self.layout.addWidget(self.button_add, 5, 2, 1, 2)

        self.setLayout(self.layout)

    def add_employee(self):
        #добавление нового сотрудника
        service = AddEmployeeService()
        role = self.combo_role.currentText()
        role_value = UserRole.EMPLOYEE if role == "Сотрудник" else UserRole.BOSS
        result = service.add_employee(
            self.input_first_name.text(),
            self.input_last_name.text(),
            self.input_surname.text(),
            self.input_phone_number.text(),
            self.input_birthday.text(),
            self.input_passport.text(),
            self.input_place_of_registration.text(),
            self.input_place_of_residence.text(),
            self.input_family.text(),
            self.input_conscription.text(),
            self.input_education.text(),
            self.input_login.text(),
            self.input_password.text(),
            role_value
        )
        if result:
            QtWidgets.QMessageBox.information(self, "Успех", "Сотрудник успешно добавлен!")
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Не удалось добавить сотрудника.")