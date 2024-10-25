class User_Data():
    def __init__(self, First_name, Last_name, Surname, Login, Password):
        self.First_name = str(First_name)
        self.Last_name = str(Last_name)
        self.Surname = str(Surname)
        self.Login = str(Login)
        self.Password = str(Password)

    @property
    def full_name(self):
        return f"{self.First_name} {self.Last_name} {self.Surname}"