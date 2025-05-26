from PyQt6 import QtWidgets, QtCore
from Service.db_service import DatabaseService
from View.add_employee_window import AddEmployeeWindow
from View.worker_details_window import WorkerDetailsWindow

class AllWorkersService:
    def __init__(self, ui):
        #инициализация сервиса для работы с сотрудниками
        self.ui = ui

    def load_workers(self):
        #список всех сотрудников
        db_service = DatabaseService()
        query_result = db_service.get_all_workers()
        count_result = db_service.get_workers_count()
        
        if query_result.error:
            QtWidgets.QMessageBox.critical(self.ui, "Ошибка", "Не удалось загрузить сотрудников.")
            return
            
        workers = query_result.result
        self.ui.listWidget.clear()
        for worker in workers:
            item = QtWidgets.QListWidgetItem(f"{worker[0]}")
            item.setData(QtCore.Qt.ItemDataRole.UserRole, worker[1])
            self.ui.listWidget.addItem(item)
        
        # Обновляем метку с количеством работников
        if count_result.result:
            self.ui.label_worker_count.setText(f"Всего работников: {count_result.result}")

    def load_worker_details(self, details_window):
        #детали сотрудника
        db_service = DatabaseService()
        query_result = db_service.get_worker_details(details_window.worker_id)
        if query_result.error:
            QtWidgets.QMessageBox.critical(details_window.centralwidget, "Ошибка", "Не удалось загрузить детали сотрудника.")
            return
        worker = query_result.result
        if worker:
            role_name = "Начальник" if worker[8] == 2 else "Сотрудник"
            details_window.label_name.setText(f"{worker[0]} {worker[1]} {worker[2]}")
            details_window.label_role.setText(f"Роль: {role_name}")
            details_window.label_phone_number.setText(f"Телефон: {worker[3]}")
            details_window.label_birthday.setText(f"День рождения: {worker[4]}")
            details_window.label_passport.setText(f"Паспорт: {worker[5]}")
            details_window.label_place_of_registration.setText(f"Прописка: {worker[6]}")
            details_window.label_place_of_residence.setText(f"Проживание: {worker[7]}")
            details_window.label_family.setText(f"Семейное положение: {worker[9]}")
            details_window.label_conscription.setText(f"Воинская обязанность: {worker[10]}")
            details_window.label_education.setText(f"Образование: {worker[11]}")

    def delete_worker(self, worker_id, details_window):
        #удаление сотрудника
        db_service = DatabaseService()
        query_result = db_service.delete_worker(worker_id)
        if query_result:
            QtWidgets.QMessageBox.information(details_window.centralwidget, "Успех", "Сотрудник успешно удален!")
            self.load_workers()
            details_window.close()
        else:
            QtWidgets.QMessageBox.critical(details_window.centralwidget, "Ошибка", "Не удалось удалить сотрудника.")

    def open_add_employee_window(self):
        #окно добавления сотрудника
        self.add_employee_window = AddEmployeeWindow()
        self.add_employee_window.show()
        self.add_employee_window.finished.connect(self.load_workers)

    def show_employee_details(self, item):
        #детали сотрудника
        worker_id = item.data(QtCore.Qt.ItemDataRole.UserRole)
        self.details_window = WorkerDetailsWindow(worker_id, self)
        self.details_window.show()

    def on_worker_details_close(self):
        #обновление списка сотрудников при закрытии окна деталей сотрудника
        self.load_workers()