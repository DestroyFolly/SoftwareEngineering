class gymService:
    def __init__(self, repo):
        self.repo = repo


    def getgymbyid(self, id):
        gym = self.repo.getgymbyid(id)

        if gym is not None:
            return gym
        else:
            return "Тренировка не найдена"


    def getlistofgyms(self, adr):
        gyms = self.repo.getlistofgyms(adr)

        if gyms is not None:
            return gyms
        else:
            return "Подходящий зал не найдем"
