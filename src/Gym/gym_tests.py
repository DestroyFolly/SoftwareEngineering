import unittest
from unittest.mock import MagicMock

from service import gymService
from model import Gym

class TestgymService(unittest.TestCase):

    def setup(self):
        self.repo = MagicMock()
        self.service = gymService(self.repo)

    def test_getbyid_success(self):
        gym = Gym(ID="1", Adres="1000", Time="10:00", Phone="111")
        self.repo.GetgymByID.return_value = gym

        result = self.service.getgymbyid("1")
        self.assertEqual(result, gym)

    def test_getbyid_failure(self):
        gym = Gym(ID="1", Adres="1000", Time="10:00", Phone="111")
        self.repo.GetgymByID.return_value = "Тренировка не найдена"

        result = self.service.getgymbyid("-5")
        self.assertEqual(result, "Тренировка не найдена")

    def test_list_success(self):
        gyms = Gym(ID="1", Adres="1000", Time="10:00", Phone="111")
        self.repo.GetListOfgyms.return_value = gyms

        result = self.service.getlistofgyms("10.04.24")
        self.assertEqual(result, gyms)

    def test_list_failure(self):
        gym = Gym(ID="1", Adres="1000", Time="10:00", Phone="111")
        self.repo.GetListOfgyms.return_value = "В эту дату нет тренировок"

        result = self.service.getlistofgyms("-5")
        self.assertEqual(result, "В эту дату нет тренировок")




if __name__ == '__main__':
    unittest.main()