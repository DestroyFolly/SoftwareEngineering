from __future__ import annotations

import unittest

from unittest.mock import MagicMock

from Gym.model import Gym
from Gym.service import GymService


class TestgymService(unittest.TestCase):

    def setup(self) -> None:
        self.repo = MagicMock()
        self.service = GymService(self.repo)

    def test_getbyid_success(self) -> None:
        gym = Gym(id=1, adress="1000", time="10:00", phone=111)
        self.repo.GetgymByid.return_value = gym

        result = self.service.getgymbyid(1)
        self.assertEqual(result, gym)

    def test_getbyid_failure(self) -> None:
        Gym(id=1, adress="1000", time="10:00", phone=111)
        self.repo.GetgymByid.return_value = "Тренировка не найдена"

        result = self.service.getgymbyid(-5)
        self.assertEqual(result, "Тренировка не найдена")

    def test_list_success(self) -> None:
        gyms = Gym(id=1, adress="1000", time="10:00", phone=111)
        self.repo.GetListOfgyms.return_value = gyms

        result = self.service.getlistofgyms("15:00")
        self.assertEqual(result, gyms)

    def test_list_failure(self) -> None:
        Gym(id=1, adress="1000", time="10:00", phone=111)
        self.repo.GetListOfgyms.return_value = "-"

        result = self.service.getlistofgyms("-5")
        self.assertEqual(result, "-")




if __name__ == '__main__':
    unittest.main()