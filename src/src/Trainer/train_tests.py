from __future__ import annotations

import unittest

from unittest.mock import MagicMock

from Trainer.model import Trainer
from Trainer.service import TrainerService


class TesttrainerService(unittest.TestCase):

    def setup(self) -> None:
        self.repo = MagicMock()
        self.service = TrainerService(self.repo)

    def test_getbyid_success(self) -> None:
        trainer = Trainer(id=1, gender="m", name="Iliyasov", surname="Khamzat", phone=9775374232, position_id = 1, gym_id=2)
        self.repo.GettrainerByid.return_value = trainer

        result = self.service.gettrainerbyid(1)
        self.assertEqual(result, trainer)

    def test_getbyid_failure(self) -> None:
        Trainer(id=1, gender="m", name="Iliyasov", surname="Khamzat", phone=9775374232, position_id = 1, gym_id=2)
        self.repo.GettrainerByid.return_value = "-"

        result = self.service.gettrainerbyid(-5)
        self.assertEqual(result, "-")

    def test_list_success(self) -> None:
        trainers = Trainer(id=1, gender="m", name="Iliyasov", surname="Khamzat", phone=9775374232, position_id = 1, gym_id=2)
        self.repo.GetListOftrainers.return_value = trainers

        result = self.service.getlistoftrainers("m")
        self.assertEqual(result, trainers)

    def test_list_failure(self) -> None:
        Trainer(id=1, gender="m", name="Iliyasov", surname="Khamzat", phone=9775374232, position_id = 1, gym_id=2)
        self.repo.GetListOftrainers.return_value = "-"

        result = self.service.getlistoftrainers("f")
        self.assertEqual(result, "-")




if __name__ == '__main__':
    unittest.main()