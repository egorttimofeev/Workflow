from PyQt6 import QtWidgets, QtCore
from View.all_workers_w_service import AllWorkersService

class AllWorkersWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Все работники")
        self.setGeometry(100, 100, 500, 300)

        #вертикальный макет
        self.layout = QtWidgets.QVBoxLayout()

        #центральный виджет
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        #настраиваем список сотрудников
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 450, 200))
        self.listWidget.setObjectName("listWidget")

        #настраиваем кнопку для добавления сотрудника
        self.button_add_employee = QtWidgets.QPushButton("Добавить работника", self.centralwidget)
        self.button_add_employee.setGeometry(QtCore.QRect(20, 240, 148, 32))
        self.button_add_employee.setObjectName("button_add_employee")
        self.button_add_employee.setStyleSheet("background-color: lightblue;")

        #инициализируем сервис для работы с сотрудниками
        self.service = AllWorkersService(self)
        self.service.load_workers()

        #сигналы к соответствующим методам
        self.listWidget.itemDoubleClicked.connect(self.service.show_employee_details)
        self.button_add_employee.clicked.connect(self.service.open_add_employee_window)