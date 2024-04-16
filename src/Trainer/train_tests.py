import unittest
from unittest.mock import MagicMock

from service import TrainerService
from model import Trainer

class TesttrainerService(unittest.TestCase):

    def setup(self):
        self.repo = MagicMock()
        self.service = TrainerService(self.repo)

    def test_getbyid_success(self):
        trainer = Trainer(ID="1", Gender="m", Name="Iliyasov", Surname="Khamzat", phone="9775374232")
        self.repo.GettrainerByID.return_value = trainer

        result = self.service.gettrainerbyid("1")
        self.assertEqual(result, trainer)

    def test_getbyid_failure(self):
        trainer = Trainer(ID="1", Gender="m", Name="Iliyasov", Surname="Khamzat", phone="9775374232")
        self.repo.GettrainerByID.return_value = "Тренировка не найдена"

        result = self.service.gettrainerbyid("-5")
        self.assertEqual(result, "Тренировка не найдена")

    def test_list_success(self):
        trainers = Trainer(ID="1", Gender="m", Name="Iliyasov", Surname="Khamzat", phone="9775374232")
        self.repo.GetListOftrainers.return_value = trainers

        result = self.service.getlistoftrainers("10.04.24")
        self.assertEqual(result, trainers)

    def test_list_failure(self):
        trainer = Trainer(ID="1", Gender="m", Name="Iliyasov", Surname="Khamzat", phone="9775374232")
        self.repo.GetListOftrainers.return_value = "В эту дату нет тренировок"

        result = self.service.getlistoftrainers("-5")
        self.assertEqual(result, "В эту дату нет тренировок")




if __name__ == '__main__':
    unittest.main()