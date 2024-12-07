from PyQt6 import QtCore, QtGui, QtWidgets
from View_service.activities_w_service import *

class Activities_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.Activities_Ui()

    def Activities_Ui(self):
        self.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 10, 141, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Назад")
        self.pushButton.clicked.connect(lambda: open_user_info_window(self))

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 271, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.task_time = QtWidgets.QSpinBox(self.centralwidget)
        self.task_time.setGeometry(QtCore.QRect(20, 160, 277, 24))
        self.task_time.setObjectName("task_time")
        self.task_time.setRange(0, 999)

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(20, 105, 277, 24))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setObjectName("dateEdit")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 270, 113, 32 ))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Добавить")
        self.pushButton_3.clicked.connect(lambda: add_activity(self))


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 25, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Занятие:")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 200, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Выполнение занятия (мин.)")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 200, 141, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setText("Занятое время")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 230, 141, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setText("Свободное время")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 320, 200, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Время на работу:")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 350, 200, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Время на отдых:")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 200, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Общее время:")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(300, 50, 341, 345))
        self.listWidget.setObjectName("listWidget")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.activities = []
        self.total_time = 0
        self.busy_time = 0
        self.free_time = 0

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Добавить занятия"))
