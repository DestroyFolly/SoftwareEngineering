from __future__ import annotations

import unittest

from unittest.mock import MagicMock

from User.model import User
from User.service import UserService


class TestUserService(unittest.TestCase):

    def setUp(self) -> None:
        self.repo = MagicMock()
        self.service = UserService(self.repo)

    def test_login_success(self) -> None:
        user = User(id=1, phone= 100, email="user@email.com", name="Pavel", surname="Maslukov", password="password", role="Admin", gender = "male")
        self.repo.GetUserByemail.return_value = user

        result = self.service.login("111","user@email.com")
        self.assertEqual(result, user)

    def test_login_user_not_found(self) -> None:
        self.repo.GetUserByemail.return_value = None

        result = self.service.login("111","user@email.com")
        self.assertEqual("user not found", result)

    def test_login_error_from_repo(self) -> None:
        user = User(id=1, phone=100, email="user@email.com", name="Pavel", surname="Maslukov", password="password",
                    role="Admin", gender = "male")
        self.repo.GetUserByemail.return_value = "repo error"

        result = self.service.login("111","user@email.com")
        self.assertEqual(result, user)



    def test_register_already_exist(self) -> None:
        user = User(id=1, phone= 100, email="user@email.com", name="Pavel", surname="Maslukov", password="password", role="Admin", gender = "male")
        self.repo.GetUserByemail.return_value = user

        self.repo.Create.return_value = user

        result = self.service.register(1, 87775462345, "user@email.com", "Pavel", "Maslukov", "password", "admin", gender = "male")

        self.assertEqual(result, "user already registered")

    def test_register_success(self) -> None:
        user = User(id=1, phone= 100, email="user@email.com", name="Pavel", surname="Maslukov", password="password", role="Admin", gender = "male")
        self.repo.GetUserByemail.return_value = None

        self.repo.Create.return_value = user

        result = self.service.register(1, 87775462345, "user@email.com", "Pavel", "Maslukov", "password", "admin", gender = "male")

        self.assertEqual(result, user)

    def test_register_failure(self) -> None:
        User(id=1, phone= 100, email="user@email.com", name="Pavel", surname="Maslukov", password="password", role="Admin", gender = "male")
        self.repo.GetUserByemail.return_value = None

        self.repo.Create.return_value = 1

        result = self.service.register(1, 87775462345, "user@email.com", "Pavel", "Maslukov", "password", "admin", gender = "male")

        self.assertEqual(result, 1)



if __name__ == '__main__':
    unittest.main()
