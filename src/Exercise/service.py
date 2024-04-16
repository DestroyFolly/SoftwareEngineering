class ExerciseService:
    def __init__(self, repo):
        self.repo = repo


    def getexbyid(self, id):
        ex = self.repo.getexbyid(id)

        if ex is not None:
            return ex
        else:
            return "Упражнение не было найдено"

    def getexbyname(self, name):
        ex = self.repo.getexbyname(name)

        if ex is not None:
            return ex
        else:
            return "Упражнение не было найдено"

    def listexercise(self, difficulty):
        exs, err = self.repo.getlistoftrains(difficulty)

        if err is not None:
            return None, err

        return exs, None
