class Holiday_Data():
    def __init__(self, Holiday_name, Holiday_date):
        self.Holiday_name = str(Holiday_name)
        self.Holiday_date = str(Holiday_date)

    def get_holiday_name(self):
        return self.Holiday_name

    def set_holiday_name(self, holiday_name):
        self.Holiday_name = str(holiday_name)

    def get_holiday_date(self):
        return self.Holiday_date

    def set_holiday_date(self, holiday_date):
        self.Holiday_date = str(holiday_date)