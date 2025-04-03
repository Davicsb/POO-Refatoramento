class WorkoutManager:
    def __init__(self):
        self._workouts = []

    @property
    def workouts(self):
        return self._workouts

    def create_workout(self):
        name = input("Nome do treino: ").strip()
        description = input("Descrição do treino: ").strip()
        if name and description:
            self._workouts.append({"Nome": name, "Descrição": description})
            print("Treino adicionado com sucesso!")
        else:
            print("Erro: Nome e descrição não podem estar vazios.")