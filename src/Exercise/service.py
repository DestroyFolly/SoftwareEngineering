class ExerciseService:
    def __init__(self, repo):
        self.repo = repo


    def GetExByID(self, id):
        user, err = self.repo.GetExByID(id)

        if err is not None:
            return None, err

        return user, None

    def ListExercise(self, difficulty):
        exs, err = self.repo.GetListOfTrains(difficulty)

        if err is not None:
            return None, err

        return exs, None
