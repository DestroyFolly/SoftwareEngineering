class ExerciseService:
    def __init__(self, repo):
        self.repo = repo


    def GetExByID(self, id):
        ex = self.repo.GetExByID(id)

        if ex is not None:
            return ex
        else:
            return "Упражнение не было найдено"

    def GetExByName(self, name):
        ex = self.repo.GetExByName(name)

        if ex is not None:
            return ex
        else:
            return "Упражнение не было найдено"

    def ListExercise(self, difficulty):
        exs, err = self.repo.GetListOfTrains(difficulty)

        if err is not None:
            return None, err

        return exs, None
