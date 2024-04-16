class TrainService:
    def __init__(self, repo):
        self.repo = repo


    def gettrainbyid(self, id):
        train = self.repo.gettrainbyid(id)

        if train is not None:
            return train
        else:
            return "Тренировка не найдена"


    def getlistoftrains(self, date):
        trains = self.repo.getlistoftrains(date)

        if trains is not None:
            return trains
        else:
            return "В эту дату нет тренировок"
