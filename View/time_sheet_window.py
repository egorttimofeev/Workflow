import sys
import os
from PyQt6 import QtCore, QtWidgets
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from View.time_sheet_w_service import *

class TimeSheet(QtWidgets.QMainWindow):
    def __init__(self, login):
        super().__init__()
        self.ui = TimeSheetUI()
        self.ui.setup_ui(self, login)

class TimeSheetUI(object):
    def setup_ui(self, main_window, login):
        main_window.setObjectName("MainWindow")
        main_window.resize(657, 430)
        
        #центральный виджет
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        #настраиваем кнопку "Назад"
        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(QtCore.QRect(510, 10, 141, 32))
        self.push_button.setObjectName("pushButton")
        self.push_button.setText("Назад")
        self.push_button.setStyleSheet("background-color: lightblue;")
        self.push_button.clicked.connect(lambda: open_user_info_window(self))

        #настраиваем календарь
        self.calendar_widget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_widget.setGeometry(QtCore.QRect(0, 0, 221, 341))
        self.calendar_widget.setObjectName("calendarWidget")

        #настраиваем кнопку "Показать"
        self.push_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_2.setGeometry(QtCore.QRect(60, 350, 113, 32))
        self.push_button_2.setObjectName("pushButton_2")
        self.push_button_2.setText("Показать")
        self.push_button_2.setStyleSheet("background-color: lightblue;")
        self.push_button_2.clicked.connect(lambda: show_employees(self))

        #настраиваем список сотрудников
        self.list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget.setGeometry(QtCore.QRect(230, 100, 400, 291))
        self.list_widget.setObjectName("listWidget")
        self.list_widget.itemDoubleClicked.connect(lambda item: show_employee_details(self, item))

        #центральный виджет
        main_window.setCentralWidget(self.centralwidget)

        #настраиваем статусную строку
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Табель учета"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TimeSheet("login")
    window.show()
    sys.exit(app.exec())