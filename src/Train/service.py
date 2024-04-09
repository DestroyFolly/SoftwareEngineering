class TrainService:
    def __init__(self, repo):
        self.repo = repo


    def GetTrainByID(self, id):
        train, err = self.repo.GetTrainByID(id)

        if err is not None:
            return None, err

        return train, None


    def GetListOfTrains(self, date):
        trains, err = self.repo.GetListOfTrains(date)

        if err is not None:
            return None, err

        return trains, None
