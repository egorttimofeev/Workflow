from PyQt6 import QtCore, QtWidgets
import sys
from user_info import UserInfoWindow
from View.window_activities import MainWindow as EmployeeMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 10, 141, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Личный кабинет")
        self.pushButton.clicked.connect(self.open_user_info_window)

        self.pushButton_add_activity = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_add_activity.setGeometry(QtCore.QRect(510, 50, 141, 32))
        self.pushButton_add_activity.setObjectName("pushButton_add_activity")
        self.pushButton_add_activity.setText("Добавить занятия")
        self.pushButton_add_activity.clicked.connect(self.add_activity)

        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 221, 341))
        self.calendarWidget.setObjectName("calendarWidget")

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 350, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(230, 100, 400, 291))
        self.listWidget.setObjectName("listWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.show_employees)
        self.listWidget.itemClicked.connect(self.show_employee_details)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Табель учета"))
        self.pushButton.setText(_translate("MainWindow", "Личный кабинет"))
        self.pushButton_2.setText(_translate("MainWindow", "Показать"))

    def show_employees(self):
        self.listWidget.clear()
        # This is where you would query the database for employees who logged activities on the selected date
        # For now, we'll leave it empty for database integration later

    def show_employee_details(self, item):
        employee_name = item.text().split(" - ")[0]
        self.details_window = QtWidgets.QWidget()
        self.details_ui = Ui_EmployeeDetails()
        self.details_ui.setupUi(self.details_window, employee_name)
        self.details_window.show()

    def open_user_info_window(self):
        self.user_info_window = UserInfoWindow(self.login)
        self.user_info_window.show()
        self.close()

    def add_activity(self):
        self.employee_window = EmployeeMainWindow(self.login)
        self.employee_window.show()
        self.close()

class Ui_EmployeeDetails(object):
    def setupUi(self, DetailsWindow, employee_name):
        DetailsWindow.setObjectName("DetailsWindow")
        DetailsWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(parent=DetailsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 20, 200, 20))
        self.label_name.setObjectName("label_name")
        self.label_name.setText(f"ФИО: {employee_name}")

        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 360, 150))
        self.listWidget.setObjectName("listWidget")

        self.label_work_time = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_work_time.setGeometry(QtCore.QRect(20, 220, 200, 20))
        self.label_work_time.setObjectName("label_work_time")

        self.label_free_time = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_free_time.setGeometry(QtCore.QRect(20, 250, 200, 20))
        self.label_free_time.setObjectName("label_free_time")

        self.label_total_time = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_total_time.setGeometry(QtCore.QRect(20, 280, 200, 20))
        self.label_total_time.setObjectName("label_total_time")

        DetailsWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(DetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(DetailsWindow)

        self.show_employee_activities()

    def retranslateUi(self, DetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        DetailsWindow.setWindowTitle(_translate("DetailsWindow", "Employee Details"))

    def show_employee_activities(self):
        # This is where you would query the database for the employee's activities
        # For now, we'll leave it empty for database integration later
        work_time = 0
        free_time = 0
        total_time = work_time + free_time
        self.label_work_time.setText(f"Рабочее время: {work_time} ч.")
        self.label_free_time.setText(f"Свободное время: {free_time} ч.")
        self.label_total_time.setText(f"Общее время: {total_time} ч.")

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, login, parent=None):
        super(MainWindow, self).__init__(parent)
        self.login = login
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = "example_login"  # Замените на реальный логин пользователя
    main_window = MainWindow(login)
    main_window.show()
    sys.exit(app.exec())
