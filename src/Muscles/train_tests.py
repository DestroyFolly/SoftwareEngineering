import unittest
from unittest.mock import MagicMock

from service import muscleService
from model import Muscle

class TestmuscleService(unittest.TestCase):

    def setup(self):
        self.repo = MagicMock()
        self.service = muscleService(self.repo)

    def test_getbyid_success(self):
        muscle = Muscle(ID="1", Title="Legs", Difficulty="3")
        self.repo.GetmuscleByID.return_value = muscle

        result = self.service.getmusclebyid("1")
        self.assertEqual(result, muscle)

    def test_getbyid_failure(self):
        muscle = Muscle(ID="1", Title="Legs", Difficulty="3")
        self.repo.GetmuscleByID.return_value = "Группа не найдена"

        result = self.service.getmusclebyid("-5")
        self.assertEqual(result, "Группа не найдена")

    def test_list_success(self):
        muscles = Muscle(ID="1", Title="Legs", Difficulty="3")
        self.repo.GetListOfmuscles.return_value = muscles

        result = self.service.getlistofmuscles("3")
        self.assertEqual(result, muscles)

    def test_list_failure(self):
        muscle = Muscle(ID="1", Title="Legs", Difficulty="3")
        self.repo.GetListOfmuscles.return_value = "Нет групп"

        result = self.service.getlistofmuscles("-5")
        self.assertEqual(result, "Нет групп")




if __name__ == '__main__':
    unittest.main()