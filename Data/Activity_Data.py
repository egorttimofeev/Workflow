class Activity_Data():
    def __init__(self, Activity_name, Duration):
        self.Activity_name = Activity_name
        self.Duration = Duration

    def get_activity_name(self):
        return self.Activity_name

    def set_activity_name(self, activity_name):
        self.Activity_name = activity_name

    def get_duration(self):
        return self.Duration

    def set_duration(self, duration):
        self.Duration = duration
