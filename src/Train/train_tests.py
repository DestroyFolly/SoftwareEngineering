import unittest
from unittest.mock import MagicMock

from service import TrainService
from model import Train

class TestTrainService(unittest.TestCase):

    def setUp(self):
        self.repo = MagicMock()
        self.service = TrainService(self.repo)

    def test_getbyid_success(self):
        train = Train(ID="1", Cost="1000", Time="10:00", Date="10.04.24", Trainer="Khamzat Iliyasov")
        self.repo.GetTrainByID.return_value = train

        result = self.service.GetTrainByID("1")
        self.assertEqual(result, train)

    def test_getbyid_failure(self):
        train = Train(ID="1", Cost="1000", Time="10:00", Date="10.04.24", Trainer="Khamzat Iliyasov")
        self.repo.GetTrainByID.return_value = "Тренировка не найдена"

        result = self.service.GetTrainByID("-5")
        self.assertEqual(result, "Тренировка не найдена")

    def test_list_success(self):
        trains = Train(ID="1", Cost="1000", Time="10:00", Date="10.04.24", Trainer="Khamzat Iliyasov")
        self.repo.GetListOfTrains.return_value = trains

        result = self.service.GetListOfTrains("10.04.24")
        self.assertEqual(result, trains)

    def test_list_failure(self):
        train = Train(ID="1", Cost="1000", Time="10:00", Date="10.04.24", Trainer="Khamzat Iliyasov")
        self.repo.GetListOfTrains.return_value = "В эту дату нет тренировок"

        result = self.service.GetListOfTrains("-5")
        self.assertEqual(result, "В эту дату нет тренировок")




if __name__ == '__main__':
    unittest.main()