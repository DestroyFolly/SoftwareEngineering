class TrainService:
    def __init__(self, repo):
        self.repo = repo


    def GetTrainByID(self, id):
        train = self.repo.GetTrainByID(id)

        if train is not None:
            return train
        else:
            return "Тренировка не найдена"


    def GetListOfTrains(self, date):
        trains = self.repo.GetListOfTrains(date)

        if trains is not None:
            return trains
        else:
            return "В эту дату нет тренировок"
