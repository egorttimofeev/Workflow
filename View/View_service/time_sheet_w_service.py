from PyQt6 import QtWidgets, QtCore
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.db_service import get_time_sheet

def open_user_info_window(self, login):
    from View.user_info_window import UserInfoWindow
    self.user_info_window = UserInfoWindow(login)
    self.user_info_window.show()
    self.centralwidget.window().close()

def add_activity(self, login):
    from View.activities_window import MainWindow as EmployeeMainWindow
    self.employee_window = EmployeeMainWindow(login)
    self.employee_window.show()
    self.centralwidget.window().close()

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

class Ui_EmployeeDetails(object):
    def setupUi(self, DetailsWindow, employee_name):
        DetailsWindow.setObjectName("DetailsWindow")
        DetailsWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(DetailsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 20, 200, 20))
        self.label_name.setObjectName("label_name")
        self.label_name.setText(f"ФИО: {employee_name}")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 360, 150))
        self.listWidget.setObjectName("listWidget")

        self.label_work_time = QtWidgets.QLabel(self.centralwidget)
        self.label_work_time.setGeometry(QtCore.QRect(20, 220, 200, 20))
        self.label_work_time.setObjectName("label_work_time")

        self.label_free_time = QtWidgets.QLabel(self.centralwidget)
        self.label_free_time.setGeometry(QtCore.QRect(20, 250, 200, 20))
        self.label_free_time.setObjectName("label_free_time")

        self.label_total_time = QtWidgets.QLabel(self.centralwidget)
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