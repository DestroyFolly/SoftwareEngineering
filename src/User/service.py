import model


class UserService:
    def __init__(self, repo):
        self.repo = repo

    def NewUserService(repo):
        return UserService(repo)

    def Login(self, email):
        user = self.repo.GetUserByEmail(email)


        if user is None:
            return "user not found"

        else:
            return user

    def Register(self, email, password):
        user = self.repo.GetUserByEmail(email)

        if user is not None:
            return "user already registered"

        new_user = model.User(Email=email, Password=password)
        err = self.repo.Create(new_user)

        if err is not None:
            return err

        return new_user

    def GetUserByID(self, ctx, id):
        user, err = self.repo.GetUserByID(id)

        if err is not None:
            return err

        return user
