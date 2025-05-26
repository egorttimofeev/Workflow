from PyQt6 import QtWidgets, QtCore
import sys
import os
import pandas as pd
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.db_service import *
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtGui import QTextDocument, QPageSize 
from PyQt6.QtGui import QPainter


def open_user_info_window(self):
    #окно информации о пользователе
    from View.user_info_window import UserInfoWindow
    self.user_info_window = UserInfoWindow()
    self.user_info_window.show()
    self.centralwidget.window().close()

def show_employees(self):
    #список сотрудников на выбранную дату
    self.list_widget.clear()
    selected_date = self.calendar_widget.selectedDate().toString("yyyy-MM-dd")
    db_service = DatabaseService()
    query_result = db_service.get_activities_by_date(selected_date)
    
    if query_result.error:
        QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", f"Ошибка получения данных: {query_result.error}")
        return

    activities = query_result.result
    user_activities = {}
    
    for activity in activities:
        user_id = activity[0]
        full_name = activity[1]
        duration = activity[2]
        if user_id not in user_activities:
            user_activities[user_id] = {
                'full_name': full_name,
                'total_time': 0
            }
        user_activities[user_id]['total_time'] += duration

    for user_id, data in user_activities.items():
        hours, minutes = divmod(data['total_time'], 60)
        self.list_widget.addItem(f"{data['full_name']} - {hours} час. {minutes} мин.")

def show_employee_details(self, item):
    #детали сотрудника
    employee_name = item.text().split(" - ")[0]
    selected_date = self.calendar_widget.selectedDate().toString("yyyy-MM-dd")
    self.details_window = QtWidgets.QMainWindow()
    self.details_ui = UiEmployeeDetails()
    self.details_ui.setupUi(self.details_window, employee_name, selected_date)
    self.details_window.show()

class UiEmployeeDetails(object):
    def setupUi(self, DetailsWindow, employee_name, selected_date):
        #пользовательский интерфейс для деталей сотрудника
        self.employee_name = employee_name
        self.selected_date = selected_date
        
        DetailsWindow.setObjectName("DetailsWindow")
        DetailsWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(DetailsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 20, 200, 20))
        self.label_name.setObjectName("label_name")
        self.label_name.setText(f"{employee_name}")
        
        #кнопка печати (была кнопка экспорта в PDF)
        self.print_button = QtWidgets.QPushButton("Распечатать", self.centralwidget)
        self.print_button.setGeometry(QtCore.QRect(120, 20, 130, 32))
        self.print_button.setObjectName("print_button")
        self.print_button.setStyleSheet("background-color: lightblue;")
        self.print_button.clicked.connect(self.show_print_dialog)
        
        #кнопка экспорта в Excel
        self.export_button = QtWidgets.QPushButton("Экспорт в Excel", self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(250, 20, 130, 32))
        self.export_button.setObjectName("export_button")
        self.export_button.setStyleSheet("background-color: lightblue;")
        self.export_button.clicked.connect(self.show_export_dialog)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 360, 150))
        self.listWidget.setObjectName("listWidget")

        self.label_work_time = QtWidgets.QLabel(self.centralwidget)
        self.label_work_time.setGeometry(QtCore.QRect(20, 210, 250, 20))
        self.label_work_time.setObjectName("label_work_time")

        self.label_free_time = QtWidgets.QLabel(self.centralwidget)
        self.label_free_time.setGeometry(QtCore.QRect(20, 240, 250, 20))
        self.label_free_time.setObjectName("label_free_time")

        self.label_total_time = QtWidgets.QLabel(self.centralwidget)
        self.label_total_time.setGeometry(QtCore.QRect(20, 270, 250, 20))
        self.label_total_time.setObjectName("label_total_time")

        DetailsWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(DetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(DetailsWindow)

        self.show_employee_activities(employee_name, selected_date)
        
    def show_export_dialog(self):
        #окно для выбора периода экспорта
        dialog = QtWidgets.QDialog(self.centralwidget)
        dialog.setWindowTitle("Выберите даты начала и окончания экспорта")
        dialog.setMinimumSize(400, 200)
        
        layout = QtWidgets.QVBoxLayout()
        
        #выбор даты начала
        start_date_layout = QtWidgets.QHBoxLayout()
        start_date_label = QtWidgets.QLabel("Дата начала:")
        self.start_date_edit = QtWidgets.QDateEdit()
        self.start_date_edit.setCalendarPopup(True)
        self.start_date_edit.setDate(QtCore.QDate.fromString(self.selected_date, "yyyy-MM-dd"))
        start_date_layout.addWidget(start_date_label)
        start_date_layout.addWidget(self.start_date_edit)
        
        #выбор даты окончания
        end_date_layout = QtWidgets.QHBoxLayout()
        end_date_label = QtWidgets.QLabel("Дата окончания:")
        self.end_date_edit = QtWidgets.QDateEdit()
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDate(QtCore.QDate.fromString(self.selected_date, "yyyy-MM-dd"))
        end_date_layout.addWidget(end_date_label)
        end_date_layout.addWidget(self.end_date_edit)
        
        #кнопки
        button_layout = QtWidgets.QHBoxLayout()
        export_button = QtWidgets.QPushButton("Экспорт")
        export_button.setStyleSheet("background-color: lightblue;")
        cancel_button = QtWidgets.QPushButton("Отмена")
        cancel_button.setStyleSheet("background-color: lightblue;")
        button_layout.addWidget(export_button)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(start_date_layout)
        layout.addLayout(end_date_layout)
        layout.addLayout(button_layout)
        
        dialog.setLayout(layout)
        
        #cвязываем кнопки с действиями
        export_button.clicked.connect(lambda: self.export_to_excel(dialog))
        cancel_button.clicked.connect(dialog.reject)
        
        dialog.exec()
    
    def export_to_excel(self, dialog):
        start_date = self.start_date_edit.date().toString("yyyy-MM-dd")
        end_date = self.end_date_edit.date().toString("yyyy-MM-dd")
        
        #путь для сохранения файла
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.centralwidget,
            "Сохранить файл",
            f"Табель_{self.employee_name}___{start_date}-{end_date}.xlsx",
            "Excel Files (*.xlsx)"
        )
        
        if not file_path:
            return
        
        #данные за выбранный период
        db_service = DatabaseService()
        activities_data = []
        
        #поисковый запрос для всех дат в периоде
        current_date = QtCore.QDate.fromString(start_date, "yyyy-MM-dd")
        end_date_obj = QtCore.QDate.fromString(end_date, "yyyy-MM-dd")
        
        total_work_time = 0
        total_free_time = 0
        
        while current_date <= end_date_obj:
            date_str = current_date.toString("yyyy-MM-dd")
            query_result = db_service.get_activities_by_employee_and_date(self.employee_name, date_str)
            
            if not query_result.error and query_result.result:
                for activity in query_result.result:
                    activity_name = activity[0]
                    duration = activity[1]
                    is_busy = activity[2]
                    
                    activities_data.append({
                        'Дата': date_str,
                        'Активность': activity_name,
                        'Продолжительность (мин)': duration,
                        'Тип': 'Рабочее время' if is_busy else 'Свободное время'
                    })
                    
                    if is_busy:
                        total_work_time += duration
                    else:
                        total_free_time += duration
            
            current_date = current_date.addDays(1)
        
        if not activities_data:
            QtWidgets.QMessageBox.information(
                self.centralwidget,
                "Информация",
                "Нет данных для экспорта за выбранный период"
            )
            return
        
        #создание DataFrame
        df = pd.DataFrame(activities_data)
        
        total_time = total_work_time + total_free_time
        work_hours, work_minutes = divmod(total_work_time, 60)
        free_hours, free_minutes = divmod(total_free_time, 60)
        total_hours, total_minutes = divmod(total_time, 60)
        
        #Excel с двумя листами
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            #лист Детали активностей
            df.to_excel(writer, sheet_name='Детали активностей', index=False)
            
            #лист Сводка
            summary_data = {
                'Показатель': ['Сотрудник', 'Период', 'Рабочее время', 'Свободное время', 'Общее время'],
                'Значение': [
                    self.employee_name,
                    f"{start_date} - {end_date}",
                    f"{work_hours} ч. {work_minutes} мин.",
                    f"{free_hours} ч. {free_minutes} мин.",
                    f"{total_hours} ч. {total_minutes} мин."
                ]
            }
            pd.DataFrame(summary_data).to_excel(writer, sheet_name='Сводка', index=False)
            
            #настройка ширины столбцов
            for sheet_name in writer.sheets:
                worksheet = writer.sheets[sheet_name]
                for idx, col in enumerate(worksheet.columns, 1):
                    #максимальная длина текста в столбце
                    max_length = 0
                    column = col[0].column_letter
                    
                    for cell in col:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    
                    #небольшой запас и ширина
                    adjusted_width = (max_length + 2) * 1.2
                    worksheet.column_dimensions[column].width = adjusted_width
        
        QtWidgets.QMessageBox.information(
            self.centralwidget,
            "Успех",
            f"Данные успешно экспортированы в файл:\n{file_path}"
        )
        
        dialog.accept()

    def retranslateUi(self, DetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        DetailsWindow.setWindowTitle(_translate("DetailsWindow", "Информация о времени сотрудника за день"))

    def show_employee_activities(self, employee_name, selected_date):
        #активности сотрудника за выбранную дату
        db_service = DatabaseService()
        query_result = db_service.get_activities_by_employee_and_date(employee_name, selected_date)
        
        if query_result.error:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", f"Ошибка получения данных: {query_result.error}")
            return

        activities = query_result.result
        work_time = 0
        free_time = 0

        for activity in activities:
            self.listWidget.addItem(f"{activity[0]} - {activity[1]} мин.")
            if activity[2]:
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
    
    def show_print_dialog(self):
        dialog = QtWidgets.QDialog(self.centralwidget)
        dialog.setWindowTitle("Выберите даты начала и окончания для печати")
        dialog.setMinimumSize(400, 200)
        
        layout = QtWidgets.QVBoxLayout()
        
        #даты начала
        start_date_layout = QtWidgets.QHBoxLayout()
        start_date_label = QtWidgets.QLabel("Дата начала:")
        self.print_start_date_edit = QtWidgets.QDateEdit()
        self.print_start_date_edit.setCalendarPopup(True)
        self.print_start_date_edit.setDate(QtCore.QDate.fromString(self.selected_date, "yyyy-MM-dd"))
        start_date_layout.addWidget(start_date_label)
        start_date_layout.addWidget(self.print_start_date_edit)
        
        #даты окончания
        end_date_layout = QtWidgets.QHBoxLayout()
        end_date_label = QtWidgets.QLabel("Дата окончания:")
        self.print_end_date_edit = QtWidgets.QDateEdit()
        self.print_end_date_edit.setCalendarPopup(True)
        self.print_end_date_edit.setDate(QtCore.QDate.fromString(self.selected_date, "yyyy-MM-dd"))
        end_date_layout.addWidget(end_date_label)
        end_date_layout.addWidget(self.print_end_date_edit)
        
        #кнопки
        button_layout = QtWidgets.QHBoxLayout()
        print_button = QtWidgets.QPushButton("Печать")
        print_button.setStyleSheet("background-color: lightblue;")
        cancel_button = QtWidgets.QPushButton("Отмена")
        cancel_button.setStyleSheet("background-color: lightblue;")
        button_layout.addWidget(print_button)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(start_date_layout)
        layout.addLayout(end_date_layout)
        layout.addLayout(button_layout)
        
        dialog.setLayout(layout)
        
        # Связываем кнопки с действиями
        print_button.clicked.connect(lambda: self.print_report(dialog))
        cancel_button.clicked.connect(dialog.reject)
        
        dialog.exec()

    def print_report(self, dialog):
        start_date = self.print_start_date_edit.date().toString("yyyy-MM-dd")
        end_date = self.print_end_date_edit.date().toString("yyyy-MM-dd")
        
        #данные за выбранный период
        db_service = DatabaseService()
        activities_data = []
        
        #запрос для всех дат в периоде
        current_date = QtCore.QDate.fromString(start_date, "yyyy-MM-dd")
        end_date_obj = QtCore.QDate.fromString(end_date, "yyyy-MM-dd")
        
        total_work_time = 0
        total_free_time = 0
        
        while current_date <= end_date_obj:
            date_str = current_date.toString("yyyy-MM-dd")
            query_result = db_service.get_activities_by_employee_and_date(self.employee_name, date_str)
            
            if not query_result.error and query_result.result:
                for activity in query_result.result:
                    activity_name = activity[0]
                    duration = activity[1]
                    is_busy = activity[2]
                    
                    activities_data.append({
                        'date': date_str,
                        'activity': activity_name,
                        'duration': duration,
                        'type': 'Рабочее время' if is_busy else 'Свободное время'
                    })
                    
                    if is_busy:
                        total_work_time += duration
                    else:
                        total_free_time += duration
                    
            current_date = current_date.addDays(1)
    
        if not activities_data:
            QtWidgets.QMessageBox.information(
                self.centralwidget,
                "Информация",
                "Нет данных для печати за выбранный период"
            )
            return
    
        try:
            #принтер и диалог печати
            printer = QPrinter()
            printer.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
            
            print_dialog = QPrintDialog(printer, self.centralwidget)
            if print_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                document = QTextDocument()
                
                #расчет времени для отчета
                total_time = total_work_time + total_free_time
                work_hours, work_minutes = divmod(total_work_time, 60)
                free_hours, free_minutes = divmod(total_free_time, 60)
                total_hours, total_minutes = divmod(total_time, 60)
                
                #текстовый отчет
                report_text = f"""
Табель учета рабочего времени сотрудника {self.employee_name} за период {start_date} - {end_date}

АКТИВНОСТИ:
"""  
                #заголовок таблицы
                report_text += f"{'Дата':<12} {'Активность':<30} {'Мин.':<6} {'Тип':<20}\n"
                report_text += "-" * 68 + "\n"
                
                #строки с данными
                for activity in activities_data:
                    report_text += f"{activity['date']:<12} {activity['activity']:<30} {activity['duration']:<6} {activity['type']:<20}\n"
                    
                report_text += "-" * 68 + "\n"
                report_text += "\Информация:\n"
                report_text += "-" * 68 + "\n"
                report_text += f"Рабочее время:     {work_hours} ч. {work_minutes} мин.\n"
                report_text += f"Свободное время:   {free_hours} ч. {free_minutes} мин.\n"
                report_text += f"Общее время:       {total_hours} ч. {total_minutes} мин.\n"
                
                #устанавливаем текст
                document.setPlainText(report_text)
                
                painter = QPainter()
                if painter.begin(printer):
                    document.drawContents(painter)
                    painter.end()
                else:
                    raise Exception("Не удалось инициализировать принтер")
                
                dialog.accept()
            else:
                return
                
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self.centralwidget,
                "Ошибка",
                f"Не удалось выполнить печать: {str(e)}"
            )
            return