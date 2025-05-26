from PyQt6 import QtWidgets, QtCore
from View.all_workers_w_service import AllWorkersService

class AllWorkersWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Все работники")
        self.setGeometry(100, 100, 500, 340)  # Увеличил высоту для поля поиска

        #вертикальный макет
        self.layout = QtWidgets.QVBoxLayout()

        #центральный виджет
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        # Добавляем поле для поиска сотрудников
        self.search_label = QtWidgets.QLabel("Поиск:", self.centralwidget)
        self.search_label.setGeometry(QtCore.QRect(20, 20, 50, 24))
        
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setPlaceholderText("Введите имя сотрудника...")
        self.search_input.setGeometry(QtCore.QRect(70, 20, 400, 24))
        self.search_input.setObjectName("search_input")
        
        #настраиваем список сотрудников
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 55, 450, 185))  # Смещаем вниз
        self.listWidget.setObjectName("listWidget")

        #настраиваем кнопку для добавления сотрудника
        self.button_add_employee = QtWidgets.QPushButton("Добавить работника", self.centralwidget)
        self.button_add_employee.setGeometry(QtCore.QRect(20, 260, 148, 32))  # Смещаем вниз
        self.button_add_employee.setObjectName("button_add_employee")
        self.button_add_employee.setStyleSheet("background-color: lightblue;")

        #метка для отображения количества работников
        self.label_worker_count = QtWidgets.QLabel(self.centralwidget)
        self.label_worker_count.setGeometry(QtCore.QRect(200, 260, 200, 32))  # Смещаем вниз
        self.label_worker_count.setObjectName("label_worker_count")
        
        #инициализируем сервис для работы с сотрудниками
        self.service = AllWorkersService(self)
        self.service.load_workers()

        #сигналы к соответствующим методам
        self.listWidget.itemDoubleClicked.connect(self.service.show_employee_details)
        self.button_add_employee.clicked.connect(self.service.open_add_employee_window)
        self.search_input.textChanged.connect(self.filter_workers)
    
    def filter_workers(self, text):
        # Фильтрация сотрудников по тексту поиска
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if text.lower() in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)