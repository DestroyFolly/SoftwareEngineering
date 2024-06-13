from __future__ import annotations

import unittest

from unittest.mock import MagicMock

from Exercise.model import Exercise
from Exercise.service import ExerciseService


class TestTrainService(unittest.TestCase):

    def setup(self) -> None:
        self.repo = MagicMock()
        self.service = ExerciseService(self.repo)

    def test_getbyid_success(self) -> None:
        ex = Exercise(id=1, name="leg press", group="legs", difficulty="medium")
        self.repo.GetExByid.return_value = ex

        result = self.service.getexbyid(1)
        self.assertEqual(result, ex)

    def test_getbyid_failure(self) -> None:
        Exercise(id=1, name="leg press", group="legs", difficulty="medium")
        self.repo.GetExByid.return_value = "Упражнение не было найдено"

        result = self.service.getexbyid(-5)
        self.assertEqual(result, "Упражнение не было найдено")

    def test_getbyname_success(self) -> None:
        ex = Exercise(id=1, name="leg press", group="legs", difficulty="medium")
        self.repo.GetExByname.return_value = ex

        result = self.service.getexbyname("leg press")
        self.assertEqual(result, ex)

    def test_getbyname_failure(self) -> None:
        Exercise(id=1, name="leg press", group="legs", difficulty="medium")
        self.repo.GetExByname.return_value = "Упражнение не было найдено"

        result = self.service.getexbyname("rest in bed")
        self.assertEqual(result, "Упражнение не было найдено")





if __name__ == '__main__':
    unittest.main()
