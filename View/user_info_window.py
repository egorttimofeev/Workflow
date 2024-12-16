import sys
import os
# Добавляем путь к родительскому каталогу для импорта модулей
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt6 import QtCore, QtWidgets
from View.user_info_w_service import UserInfoService

class UserInfoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.service = UserInfoService(self)
        self.user_ui()

    def user_ui(self):
        # Устанавливаем размер окна
        self.resize(657, 430)
        
        # Создаем центральный виджет
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Создаем и настраиваем метки для отображения информации о пользователе
        self.label_full_name = QtWidgets.QLabel(self.centralwidget)
        self.label_full_name.setGeometry(QtCore.QRect(20, 40, 290, 30))
        self.label_full_name.setObjectName("label_full_name")

        self.label_role = QtWidgets.QLabel(self.centralwidget)
        self.label_role.setGeometry(QtCore.QRect(20, 80, 290, 30))
        self.label_role.setObjectName("label_role")

        self.label_phone_number = QtWidgets.QLabel(self.centralwidget)
        self.label_phone_number.setGeometry(QtCore.QRect(20, 120, 290, 30))
        self.label_phone_number.setObjectName("label_phone_number")

        self.label_birthday = QtWidgets.QLabel(self.centralwidget)
        self.label_birthday.setGeometry(QtCore.QRect(20, 160, 290, 30))
        self.label_birthday.setObjectName("label_birthday")

        self.label_family = QtWidgets.QLabel(self.centralwidget)
        self.label_family.setGeometry(QtCore.QRect(20, 200, 290, 30))
        self.label_family.setObjectName("label_family")

        self.label_conscription = QtWidgets.QLabel(self.centralwidget)
        self.label_conscription.setGeometry(QtCore.QRect(20, 240, 290, 30))
        self.label_conscription.setObjectName("label_conscription")

        self.label_education = QtWidgets.QLabel(self.centralwidget)
        self.label_education.setGeometry(QtCore.QRect(20, 280, 290, 30))
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

        # Создаем и настраиваем кнопки для различных действий
        self.button_tabel = QtWidgets.QPushButton("Табель учета", self.centralwidget)
        self.button_tabel.setGeometry(QtCore.QRect(510, 50, 141, 32))
        self.button_tabel.setObjectName("button_tabel")
        self.button_tabel.setStyleSheet("background-color: lightblue;")
        self.button_tabel.clicked.connect(self.service.open_time_sheet_window)

        self.button_add_activity = QtWidgets.QPushButton("Добавить занятия", self.centralwidget)
        self.button_add_activity.setGeometry(QtCore.QRect(510, 10, 141, 32))
        self.button_add_activity.setObjectName("button_add_activity")
        self.button_add_activity.setStyleSheet("background-color: lightblue;")
        self.button_add_activity.clicked.connect(self.service.open_activities_window)

        self.button_all_workers = QtWidgets.QPushButton("Все работники", self.centralwidget)
        self.button_all_workers.setGeometry(QtCore.QRect(20, 10, 148, 32))
        self.button_all_workers.setObjectName("button_all_workers")
        self.button_all_workers.setStyleSheet("background-color: lightblue;")
        self.button_all_workers.clicked.connect(self.service.open_all_workers_window)

        # Устанавливаем центральный виджет
        self.setCentralWidget(self.centralwidget)

        # Переводим текст интерфейса
        self.service.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)