from __future__ import annotations

import unittest

from unittest.mock import MagicMock

from Muscles.model import Muscle
from Muscles.service import MuscleService


class TestmuscleService(unittest.TestCase):

    def setup(self):
        self.repo = MagicMock()
        self.service = MuscleService(self.repo)

    def test_getbyid_success(self) -> None:
        muscle = Muscle(id=1, title="Legs", difficulty="Hard")
        self.repo.GetmuscleByid.return_value = muscle

        result = self.service.getmusclebyid(1)
        self.assertEqual(result, muscle)

    def test_getbyid_failure(self) -> None:
        Muscle(id=1, title="Legs", difficulty="Hard")
        self.repo.GetmuscleByid.return_value = "Группа не найдена"

        result = self.service.getmusclebyid("-5")
        self.assertEqual(result, "Группа не найдена")

    def test_list_success(self) -> None:
        muscles = Muscle(id=1, title="Legs", difficulty="Hard")
        self.repo.GetListOfmuscles.return_value = muscles

        result = self.service.getlistofmuscles("3")
        self.assertEqual(result, muscles)

    def test_list_failure(self) -> None:
        Muscle(id=1, title="Legs", difficulty="Hard")
        self.repo.GetListOfmuscles.return_value = "Нет групп"

        result = self.service.getlistofmuscles("-5")
        self.assertEqual(result, "Нет групп")




if __name__ == '__main__':
    unittest.main()