from enum import IntEnum

class User_Role(IntEnum):
    EMPLOYEE = 1
    BOSS = 2
    HR_DEPARTMENT = 3

class User:
    def __init__(self, id_user, Role, First_name, Last_name, Surname, Login, Password, Phone_number, Birthday, Passport, Place_of_registration, Place_of_residence, Family, Conscription, Education):
        self.id_user = id_user
        self.__role = int(Role)
        self.First_name = str(First_name)
        self.Last_name = str(Last_name)
        self.Surname = str(Surname)
        self.Login = str(Login)
        self.Password = str(Password)
        self.Phone_number = str(Phone_number)
        self.Birthday = str(Birthday)
        self.Passport = str(Passport)
        self.Place_of_registration = str(Place_of_registration)
        self.Place_of_residence = str(Place_of_residence)
        self.Family = str(Family)
        self.Conscription = str(Conscription)
        self.Education = str(Education)

    @property
    def full_name(self):
        return f"{self.First_name} {self.Last_name} {self.Surname}"

    @property
    def role_name(self):
        return User_Role(self.__role).name

    @property
    def Role(self):
        return self.__role

    def __get_role_name(self):
        return User_Role(self.__role).name