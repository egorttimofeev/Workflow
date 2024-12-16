from PyQt6 import QtWidgets, QtCore
from View.all_workers_w_service import *

class WorkerDetailsWindow(QtWidgets.QMainWindow):
    def __init__(self, worker_id, service):
        super().__init__()
        self.service = service
        self.worker_id = worker_id
        self.setWindowTitle("Информация о сотруднике")
        self.setGeometry(100, 100, 500, 400)

        #центральный виджет
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        #настраиваем метки для отображения информации о сотруднике
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 20, 450, 20))
        self.label_name.setObjectName("label_name")

        self.label_role = QtWidgets.QLabel(self.centralwidget)
        self.label_role.setGeometry(QtCore.QRect(20, 50, 450, 20))
        self.label_role.setObjectName("label_role")

        self.label_phone_number = QtWidgets.QLabel(self.centralwidget)
        self.label_phone_number.setGeometry(QtCore.QRect(20, 80, 450, 20))
        self.label_phone_number.setObjectName("label_phone_number")

        self.label_birthday = QtWidgets.QLabel(self.centralwidget)
        self.label_birthday.setGeometry(QtCore.QRect(20, 110, 450, 20))
        self.label_birthday.setObjectName("label_birthday")

        self.label_passport = QtWidgets.QLabel(self.centralwidget)
        self.label_passport.setGeometry(QtCore.QRect(20, 140, 450, 20))
        self.label_passport.setObjectName("label_passport")

        self.label_place_of_registration = QtWidgets.QLabel(self.centralwidget)
        self.label_place_of_registration.setGeometry(QtCore.QRect(20, 170, 450, 20))
        self.label_place_of_registration.setObjectName("label_place_of_registration")

        self.label_place_of_residence = QtWidgets.QLabel(self.centralwidget)
        self.label_place_of_residence.setGeometry(QtCore.QRect(20, 200, 450, 20))
        self.label_place_of_residence.setObjectName("label_place_of_residence")

        self.label_family = QtWidgets.QLabel(self.centralwidget)
        self.label_family.setGeometry(QtCore.QRect(20, 230, 450, 20))
        self.label_family.setObjectName("label_family")

        self.label_conscription = QtWidgets.QLabel(self.centralwidget)
        self.label_conscription.setGeometry(QtCore.QRect(20, 260, 450, 20))
        self.label_conscription.setObjectName("label_conscription")

        self.label_education = QtWidgets.QLabel(self.centralwidget)
        self.label_education.setGeometry(QtCore.QRect(20, 290, 450, 20))
        self.label_education.setObjectName("label_education")

        #настраиваем кнопку для удаления сотрудника
        self.button_delete = QtWidgets.QPushButton("Удалить", self.centralwidget)
        self.button_delete.setGeometry(QtCore.QRect(20, 330, 100, 32))
        self.button_delete.setObjectName("button_delete")
        self.button_delete.setStyleSheet("background-color: lightblue;")

        #детали сотрудника
        self.service.load_worker_details(self)

        #сигнал нажатия кнопки к методу удаления сотрудника
        self.button_delete.clicked.connect(lambda: self.service.delete_worker(self.worker_id, self))

    #закрытие окна
    def closeEvent(self, event):
        self.service.on_worker_details_close()
        event.accept()