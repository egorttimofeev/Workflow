from PyQt6 import QtCore, QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from View_service.time_sheet_w_service import *

class Time_Sheet(QtWidgets.QMainWindow):
    def __init__(self, login):
        super().__init__()
        self.ui = Time_Sheet_UI()
        self.ui.setupUi(self, login)

class Time_Sheet_UI(object):
    def setupUi(self, MainWindow, login):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 10, 141, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Личный кабинет")
        self.pushButton.clicked.connect(lambda: open_user_info_window(self))

        self.pushButton_add_activity = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_activity.setGeometry(QtCore.QRect(510, 50, 141, 32))
        self.pushButton_add_activity.setObjectName("pushButton_add_activity")
        self.pushButton_add_activity.setText("Добавить занятия")
        self.pushButton_add_activity.clicked.connect(lambda: add_activity(self))

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 221, 341))
        self.calendarWidget.setObjectName("calendarWidget")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 350, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Показать")
        self.pushButton_2.clicked.connect(lambda: show_employees(self))

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(230, 100, 400, 291))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(lambda item: show_employee_details(self, item))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Табель учета"))

def open_user_info_window(self):
    from View_win.user_info_window import UserInfoWindow  
    self.user_info_window = UserInfoWindow()
    self.user_info_window.show()
    self.centralwidget.window().close()

def add_activity(self):
    from View_win.activities_window import Activities_Window
    self.activities_window = Activities_Window()
    self.activities_window.show()
    self.centralwidget.window().close()

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
        self.label_name.setGeometry(QtCore.QRect(20, 10, 200, 30))
        self.label_name.setObjectName("label_name")
        self.label_name.setText(f"{employee_name}")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 360, 150))
        self.listWidget.setObjectName("listWidget")

        self.label_work_time = QtWidgets.QLabel(self.centralwidget)
        self.label_work_time.setGeometry(QtCore.QRect(20, 220, 250, 50))
        self.label_work_time.setObjectName("label_work_time")

        self.label_free_time = QtWidgets.QLabel(self.centralwidget)
        self.label_free_time.setGeometry(QtCore.QRect(20, 250, 250, 50))
        self.label_free_time.setObjectName("label_free_time")

        self.label_total_time = QtWidgets.QLabel(self.centralwidget)
        self.label_total_time.setGeometry(QtCore.QRect(20, 280, 250, 50))
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

        self.label_work_time.setText(f"Рабочее время: {work_hours} час. {work_minutes} мин.")
        self.label_free_time.setText(f"Свободное время: {free_hours} час. {free_minutes} мин.")
        self.label_total_time.setText(f"Общее время: {total_hours} час. {total_minutes} мин.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = "1"  # Замените на реальный логин пользователя
    main_window = Time_Sheet(login)
    main_window.show()
    sys.exit(app.exec())