class muscleService:
    def __init__(self, repo):
        self.repo = repo


    def getmusclebyid(self, id):
        muscle = self.repo.getmusclebyid(id)

        if muscle is not None:
            return muscle
        else:
            return "Тренировка не найдена"


    def getlistofmuscles(self, difficulty):
        muscles = self.repo.getlistofmuscles(difficulty)

        if muscles is not None:
            return muscles
        else:
            return "Нет таких группы мышц"
