from abc import ABC, abstractmethod

class Tracker(ABC):
    @abstractmethod
    def track(self):
        pass

    @abstractmethod
    def get_progress(self):
        pass

class ActivityTracker(Tracker):
    def __init__(self):
        self._activities = []
        self._progress = {"Passos": 0, "Calorias": 0, "Duração": 0}

    @property
    def activities(self):
        return self._activities

    @property
    def progress(self):
        return self._progress

    def track(self):
        try:
            steps = int(input("Número de passos: "))
            calories = float(input("Calorias queimadas: "))
            duration = int(input("Duração do treino (minutos): "))

            self._activities.append({"Passos": steps, "Calorias": calories, "Duração": duration})
            self._progress["Passos"] += steps
            self._progress["Calorias"] += calories
            self._progress["Duração"] += duration

            print("Atividade registrada!")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")

    def get_progress(self):
        return self._progress

class NutritionTracker(Tracker):
    def __init__(self):
        self._nutrition = []

    @property
    def nutrition(self):
        return self._nutrition

    def track(self):
        try:
            food = input("Alimento consumido: ").strip()
            calories = float(input("Calorias ingeridas: "))
            if food:
                self._nutrition.append({"Alimento": food, "Calorias": calories})
                print("Alimento registrado!")
            else:
                print("Erro: O nome do alimento não pode estar vazio.")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")

    def get_progress(self):
        return self._nutrition