from __future__ import annotations

import unittest

from unittest.mock import MagicMock

from Train.model import Train
from Train.service import TrainService


class TestTrainService(unittest.TestCase):

    def setup(self) -> None:
        self.repo = MagicMock()
        self.service = TrainService(self.repo)

    def test_getbyid_success(self) -> None:
        train = Train(id = 1, title="legs", time="10:00", date="10.04.24", trainer_id=1, gym_id = 2)
        self.repo.GetTrainByID.return_value = train

        result = self.service.gettrainbyid(1)
        self.assertEqual(result, train)

    def test_getbyid_failure(self) -> None:
        Train(id = 1, title="legs", time="10:00", date="10.04.24", trainer_id=1, gym_id = 2)
        self.repo.GetTrainByID.return_value = "-"

        result = self.service.gettrainbyid("-5")
        self.assertEqual(result, "-")

    def test_list_success(self) -> None:
        trains = Train(id = 1, title="legs", time="10:00", date="10.04.24", trainer_id=1, gym_id = 2)
        self.repo.GetListOfTrains.return_value = trains

        result = self.service.getlistoftrains("10.04.24")
        self.assertEqual(result, trains)

    def test_list_failure(self) -> None:
        Train(id = 1, title="legs", date="10.04.24", trainer_id=1, gym_id = 2)
        self.repo.GetListOfTrains.return_value = "-"

        result = self.service.getlistoftrains("-5")
        self.assertEqual(result, "-")




if __name__ == '__main__':
    unittest.main()