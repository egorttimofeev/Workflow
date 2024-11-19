from PyQt6 import QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.db_connector import add_activities_to_db

def add_activity(self, id_user, activity_name, duration, date, is_busy):
    activity_name = self.lineEdit.text()
    duration = self.task_time.value()
    date = self.dateEdit.date().toString("yyyy-MM-dd")
    is_busy = self.radioButton.isChecked()

    if activity_name and duration:
        self.listWidget.addItem(f"{activity_name} - {duration} мин. {'(Занятое время)' if is_busy else '(Свободное время)'}")
        update_times(self, duration, is_busy)
        self.activities.append({
            "id_user": id_user,
            "activity_name": activity_name,
            "duration": duration,
            "date": date,
            "trigger_work": is_busy,
            "trigger_chill": not is_busy
        })
        add_activities_to_db(id_user, activity_name, duration, date, is_busy)
        QtWidgets.QMessageBox.information(self.centralwidget, "Успех", "Занятие успешно добавлено в базу данных")
    else:
        QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", "Заполните все поля")



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

def open_user_info_window(self, id_user):
    from View.user_info_window import UserInfoWindow  
    self.user_info_window = UserInfoWindow(id_user)
    self.user_info_window.show()
    self.centralwidget.window().close()