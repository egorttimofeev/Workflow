from PyQt6 import QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.db_service import Database_Service
from Service.user_service import User_Service

def add_activity(self):
    activity_name = self.lineEdit.text().strip()
    duration = self.task_time.value()
    date = self.dateEdit.date().toString("yyyy-MM-dd")
    is_busy = self.radioButton.isChecked()
    trigger_chill = self.radioButton_2.isChecked()

    # Проверка заполненности полей
    if not activity_name:
        QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", "Введите название активности!")
        return
    if duration <= 0:
        QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", "Продолжительность должна быть больше 0!")
        return
    if not (is_busy or trigger_chill):
        QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", "Выберите тип активности (занятое или свободное время)!")
        return

    # Определение is_busy
    is_busy = 1 if is_busy else 0

    # Получение текущего авторизованного пользователя
    user_service = User_Service()
    current_user = user_service.authorised_user

    if not current_user:  # Если пользователь не авторизован
        QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", "Пользователь не авторизован!")
        return

    user_id = current_user.id_user  # Предполагаем, что у User есть атрибут Id_user

    # Добавление в базу данных
    db_service = Database_Service()
    result = db_service.add_activity_to_db(user_id, activity_name, duration, date, is_busy)

    if result.error:
        QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", f"Ошибка добавления активности: {result.error}")
        return

    # Обновляем интерфейс только при успешном добавлении
    self.listWidget.addItem(f"{activity_name} - {duration} мин. {'(Занятое время)' if is_busy else '(Свободное время)'}")
    update_times(self, duration, is_busy)
    QtWidgets.QMessageBox.information(self.centralwidget, "Успех", "Занятие успешно добавлено в базу данных")

def update_times(self, duration, is_busy):
    """
    Обновление времени в интерфейсе.
    """
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

def open_user_info_window(self):
    from View_win.user_info_window import UserInfoWindow  
    self.user_info_window = UserInfoWindow()
    self.user_info_window.show()
    self.centralwidget.window().close()