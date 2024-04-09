from enum import Enum

class UserRole(Enum):
    Admin = "admin"
    Customer = "trainer"
    Seller = "client"

class User:
    def __init__(self, ID= 0, Phone=0, Email=0, Name=0, Surname=0, Password=0, Role=0):
        self.ID = ID
        self.Email = Email
        self.Phone = Phone
        self.Name = Name
        self.Surname = Surname
        self.Password = Password
        self.Role = Role