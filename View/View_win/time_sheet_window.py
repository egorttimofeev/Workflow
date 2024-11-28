from PyQt6 import QtCore, QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from View_service.time_sheet_w_service import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, login, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, login)
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, login):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 10, 141, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Личный кабинет")
        self.pushButton.clicked.connect(lambda: open_user_info_window(self, login))

        self.pushButton_add_activity = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_activity.setGeometry(QtCore.QRect(510, 50, 141, 32))
        self.pushButton_add_activity.setObjectName("pushButton_add_activity")
        self.pushButton_add_activity.setText("Добавить занятия")
        self.pushButton_add_activity.clicked.connect(lambda: add_activity(self, login))

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
        self.listWidget.itemClicked.connect(lambda item: show_employee_details(self, item))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Табель учета"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = "1"  # Замените на реальный логин пользователя
    main_window = MainWindow(login)
    main_window.show()
    sys.exit(app.exec())