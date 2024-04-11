import unittest
from unittest.mock import MagicMock

from service import ExerciseService
from model import Exercise

class TestTrainService(unittest.TestCase):

    def setUp(self):
        self.repo = MagicMock()
        self.service = ExerciseService(self.repo)

    def test_getbyid_success(self):
        ex = Exercise(ID="1", Name="leg press", Group="legs", Difficulty="medium")
        self.repo.GetExByID.return_value = ex

        result = self.service.GetExByID("1")
        self.assertEqual(result, ex)

    def test_getbyid_failure(self):
        ex = Exercise(ID="1", Name="leg press", Group="legs", Difficulty="medium")
        self.repo.GetExByID.return_value = "Упражнение не было найдено"

        result = self.service.GetExByID("-5")
        self.assertEqual(result, "Упражнение не было найдено")

    def test_getbyname_success(self):
        ex = Exercise(ID="1", Name="leg press", Group="legs", Difficulty="medium")
        self.repo.GetExByName.return_value = ex

        result = self.service.GetExByName("leg press")
        self.assertEqual(result, ex)

    def test_getbyname_failure(self):
        ex = Exercise(ID="1", Name="leg press", Group="legs", Difficulty="medium")
        self.repo.GetExByName.return_value = "Упражнение не было найдено"

        result = self.service.GetExByName("rest in bed")
        self.assertEqual(result, "Упражнение не было найдено")





if __name__ == '__main__':
    unittest.main()
