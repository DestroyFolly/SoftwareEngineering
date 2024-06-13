from __future__ import annotations

from Gym.model import Gym


class GymService:
    def __init__(self, repo) -> None:
        self.repo = repo

    def getgymbyid(self, id) -> Gym | str:
        gym = self.repo.getgymbyid(id)

        if gym is not None:
            return gym
        else:
            return "Тренировка не найдена"

    def getlistofgyms(self) -> Gym | str:
        gyms = self.repo.getlistofgyms()

        if gyms is not None:
            return gyms
        else:
            return "Подходящий зал не найдем"
