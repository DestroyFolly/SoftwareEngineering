class ListTrainReq:
    def __init__(self, UserID, TrainId):
        self.UserID = UserID
        self.TrainId = TrainId

class AddExercise:
    def __init__(self, TrainID, ExId):
        self.TrainID = TrainID
        self.ExId = ExId

class RemoveExercise:
    def __init__(self, TrainID, ExId):
        self.TrainID = TrainID
        self.ExId = ExId
