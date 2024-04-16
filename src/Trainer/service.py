class TrainerService:
    def __init__(self, repo):
        self.repo = repo


    def gettrainerbyid(self, id):
        train = self.repo.gettrainerbyid(id)

        if train is not None:
            return train
        else:
            return "Тренир не найден"


    def getlistoftrainers(self, date):
        trains = self.repo.getlistoftrains(date)

        if trains is not None:
            return trains
        else:
            return "Нет тренеров"
