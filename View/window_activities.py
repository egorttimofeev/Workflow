from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.db_connector import add_activity_to_db
from user_info import UserInfoWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, login):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 10, 141, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Личный кабинет")
        self.pushButton.clicked.connect(lambda: self.open_user_info_window(login))

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 271, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.task_time = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.task_time.setGeometry(QtCore.QRect(20, 160, 277, 24))
        self.task_time.setObjectName("task_time")

        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(20, 105, 277, 24))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setObjectName("dateEdit")

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 200, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Добавить")
        self.pushButton_3.clicked.connect(lambda: self.add_activity(login))

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Занятие:")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 200, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Выполнение занятия (мин.)")

        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 240, 141, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setText("Занятое время")

        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 270, 141, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setText("Свободное время")

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 320, 200, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Время на работу:")

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 350, 200, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Время на отдых:")

        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 200, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Общее время:")

        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(300, 50, 341, 345))
        self.listWidget.setObjectName("listWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.total_time = 0
        self.busy_time = 0
        self.free_time = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Табель учета"))

    def add_activity(self, login):
        activity_name = self.lineEdit.text()
        duration = self.task_time.value()
        date = self.dateEdit.date().toString("yyyy-MM-dd")
        is_busy = self.radioButton.isChecked()

        if activity_name and duration:
            self.listWidget.addItem(f"{activity_name} - {duration} мин. {'(Занятое время)' if is_busy else '(Свободное время)'}")
            self.update_times(duration, is_busy)
            add_activity_to_db(login, activity_name, duration, date, is_busy)
            self.centralwidget.window().close()

    def update_times(self, duration, is_busy):
        self.total_time += duration
        if is_busy:
            self.busy_time += duration
        else:
            self.free_time += duration

        busy_hours, busy_minutes = divmod(self.busy_time, 60)
        free_hours, free_minutes = divmod(self.free_time, 60)
        total_hours, total_minutes = divmod(self.total_time, 60)

        self.label_4.setText(f"Время на работу: {busy_hours} ч. {busy_minutes} мин.")
        self.label_5.setText(f"Время на отдых: {free_hours} ч. {free_minutes} мин.")
        self.label_6.setText(f"Общее время: {total_hours} ч. {total_minutes} мин.")

    def open_user_info_window(self, login):
        self.user_info_window = UserInfoWindow(login)
        self.user_info_window.show()
        self.centralwidget.window().close()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, login, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self, login)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = "example_login"  # Замените на реальный логин пользователя
    main_window = MainWindow(login)
    main_window.show()
    sys.exit(app.exec())