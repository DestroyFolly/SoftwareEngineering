class RegisterReq:
    def __init__(self, Email, Password):
        self.Email = Email
        self.Password = Password

class RegisterRes:
    def __init__(self, User):
        self.User = User

class LoginReq:
    def __init__(self, Email, Password):
        self.Email = Email
        self.Password = Password

class LoginRes:
    def __init__(self, User):
        self.User = User


