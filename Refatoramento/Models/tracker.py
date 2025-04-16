from abc import ABC, abstractmethod
import random

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
        self._goals = {"Passos": 0, "Calorias": 0, "Duração": 0}

    @property
    def goals(self):
        return self._goals
    
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
            
    def device_sync(self):
        steps = random.randint(100, 500)
        calories = random.uniform(20, 100)
        self._progress["Passos"] += steps
        self._progress["Calorias"] += calories
        print(f"Dispositivo sincronizado! +{steps} passos e +{calories:.2f} calorias adicionados.")
    
    def set_goals(self):
        try:
            self._goals["Passos"] = int(input("Meta diária de passos: "))
            self._goals["Calorias"] = float(input("Meta diária de calorias queimadas: "))
            self._goals["Duração"] = int(input("Meta diária de duração dos treinos (min): "))
            print("Metas definidas com sucesso!")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")
            
    def execute(self):
        self.track()
    
    def check_progress(self):
        print("\nProgresso Atual:")
        for key in self._goals:
            goal = self._goals[key]
            current = self._progress[key]
            percentage = (current / goal * 100) if goal > 0 else 0
            print(f"{key}: {current} / {goal} ({percentage:.1f}%)")

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
    
    def execute(self):
        self.track()