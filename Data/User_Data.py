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

    def get_first_name(self):
        return self.First_name

    def set_first_name(self, first_name):
        self.First_name = str(first_name)

    def get_last_name(self):
        return self.Last_name

    def set_last_name(self, last_name):
        self.Last_name = str(last_name)

    def get_surname(self):
        return self.Surname

    def set_surname(self, surname):
        self.Surname = str(surname)

    def get_login(self):
        return self.Login

    def set_login(self, login):
        self.Login = str(login)

    def get_password(self):
        return self.Password

    def set_password(self, password):
        self.Password = str(password)