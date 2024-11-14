class Work_Time_Data():
    def __init__(self, Employee_id, Work_date, Hours_worked):
        self.Employee_id = int(Employee_id)
        self.Work_date = str(Work_date)
        self.Hours_worked = float(Hours_worked)

    def get_employee_id(self):
        return self.Employee_id

    def set_employee_id(self, employee_id):
        self.Employee_id = int(employee_id)

    def get_work_date(self):
        return self.Work_date

    def set_work_date(self, work_date):
        self.Work_date = str(work_date)

    def get_hours_worked(self):
        return self.Hours_worked

    def set_hours_worked(self, hours_worked):
        self.Hours_worked = float(hours_worked)
