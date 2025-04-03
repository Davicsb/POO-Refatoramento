class GoalManager:
    def __init__(self):
        self._goals = {"Passos": 0, "Calorias": 0, "Duração": 0}
        self._progress = {"Passos": 0, "Calorias": 0, "Duração": 0}

    @property
    def goals(self):
        return self._goals

    @property
    def progress(self):
        return self._progress

    def set_goals(self):
        try:
            self._goals["Passos"] = int(input("Meta diária de passos: "))
            self._goals["Calorias"] = float(input("Meta diária de calorias queimadas: "))
            self._goals["Duração"] = int(input("Meta diária de duração dos treinos (min): "))
            print("Metas definidas com sucesso!")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")

    def check_progress(self):
        print("\nProgresso Atual:")
        for key in self._goals:
            goal = self._goals[key]
            current = self._progress[key]
            percentage = (current / goal * 100) if goal > 0 else 0
            print(f"{key}: {current} / {goal} ({percentage:.1f}%)")