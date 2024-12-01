from PyQt6 import QtWidgets, QtCore
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.db_service import *

def open_user_info_window(self, login):
    from View_win.user_info_window import UserInfoWindow
    self.user_info_window = UserInfoWindow(login)
    self.user_info_window.show()
    self.centralwidget.window().close()

def add_activity(self, login):
    from View_win.activities_window import Activities_Window
    self.activities_window = Activities_Window()
    self.activities_window.show()
    self.centralwidget.window().close()

def show_employees(self):
    self.listWidget.clear()
    selected_date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
    db_service = Database_Service()
    query_result = db_service.get_activities_by_date(selected_date)
    
    if query_result.error:
        QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", f"Ошибка получения данных: {query_result.error}")
        return

    activities = query_result.result
    user_activities = {}
    
    for activity in activities:
        user_id = activity[0]  # Индекс 0 для user_id
        full_name = activity[1]  # Индекс 1 для full_name
        duration = activity[2]  # Индекс 2 для duration
        if user_id not in user_activities:
            user_activities[user_id] = {
                'full_name': full_name,
                'total_time': 0
            }
        user_activities[user_id]['total_time'] += duration

    for user_id, data in user_activities.items():
        hours, minutes = divmod(data['total_time'], 60)
        self.listWidget.addItem(f"{data['full_name']} - {hours} час. {minutes} мин.")

def show_employee_details(self, item):
    employee_name = item.text().split(" - ")[0]
    selected_date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
    self.details_window = QtWidgets.QMainWindow()
    self.details_ui = Ui_EmployeeDetails()
    self.details_ui.setupUi(self.details_window, employee_name, selected_date)
    self.details_window.show()

class Ui_EmployeeDetails(object):
    def setupUi(self, DetailsWindow, employee_name, selected_date):
        DetailsWindow.setObjectName("DetailsWindow")
        DetailsWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(DetailsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 20, 200, 20))
        self.label_name.setObjectName("label_name")
        self.label_name.setText(f"{employee_name}")

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

        self.show_employee_activities(employee_name, selected_date)

    def retranslateUi(self, DetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        DetailsWindow.setWindowTitle(_translate("DetailsWindow", "Информация о времени сотрудника за день"))

    def show_employee_activities(self, employee_name, selected_date):
        db_service = Database_Service()
        query_result = db_service.get_activities_by_employee_and_date(employee_name, selected_date)
        
        if query_result.error:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", f"Ошибка получения данных: {query_result.error}")
            return

        activities = query_result.result
        work_time = 0
        free_time = 0

        for activity in activities:
            self.listWidget.addItem(f"{activity[0]} - {activity[1]} мин.")  # Индексы для activity_name и duration
            if activity[2]:  # Индекс для is_busy
                work_time += activity[1]
            else:
                free_time += activity[1]

        total_time = work_time + free_time
        work_hours, work_minutes = divmod(work_time, 60)
        free_hours, free_minutes = divmod(free_time, 60)
        total_hours, total_minutes = divmod(total_time, 60)

        self.label_work_time.setText(f"Рабочее время: {work_hours} часов {work_minutes} минут")
        self.label_free_time.setText(f"Свободное время: {free_hours} часов {free_minutes} минут")
        self.label_total_time.setText(f"Общее время: {total_hours} часов {total_minutes} минут")