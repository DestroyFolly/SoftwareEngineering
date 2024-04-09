import unittest
from unittest.mock import MagicMock

from service import UserService
from model import User

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.repo = MagicMock()
        self.service = UserService(self.repo)

    def test_login_success(self):
        user = User(ID="1", Phone= "100", Email="user@email.com", Name="Pavel", Surname="Maslukov", Password="password", Role="Admin")
        self.repo.GetUserByEmail.return_value = user

        result = self.service.Login("user@email.com")
        self.assertEqual(result, user)

    def test_login_user_not_found(self):
        self.repo.GetUserByEmail.return_value = None

        result = self.service.Login("user@email.com")
        self.assertEqual("user not found", result)

    def test_login_error_from_repo(self):
        self.repo.GetUserByEmail.return_value = None, "repo error"

        result, err = self.service.Login("user@email.com")
        self.assertIsNone(result)
        self.assertEqual(err, "repo error")


    def test_register_already_exist(self):
        user = User(ID="1", Phone= "100", Email="user@email.com", Name="Pavel", Surname="Maslukov", Password="password", Role="Admin")
        self.repo.GetUserByEmail.return_value = user

        self.repo.Create.return_value = user

        result = self.service.Register("user@email.com", "password")

        self.assertEqual(result, "user already registered")

    def test_register_success(self):
        user = User(ID="1", Phone= "100", Email="user@email.com", Name="Pavel", Surname="Maslukov", Password="password", Role="Admin")
        self.repo.GetUserByEmail.return_value = None

        self.repo.Create.return_value = user

        result = self.service.Register("user@email.com", "password")

        self.assertEqual(result, user)

    def test_register_failure(self):
        user = User(ID="1", Phone= "100", Email="user@email.com", Name="Pavel", Surname="Maslukov", Password="password", Role="Admin")
        self.repo.GetUserByEmail.return_value = None

        self.repo.Create.return_value = 1

        result = self.service.Register("user@email.com", "password")

        self.assertEqual(result, 1)



if __name__ == '__main__':
    unittest.main()
