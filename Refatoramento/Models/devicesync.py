import random

class DeviceSync:
    def __init__(self, progress):
        self._progress = progress

    def sync_device(self):
        steps = random.randint(100, 500)
        calories = random.uniform(20, 100)
        self._progress["Passos"] += steps
        self._progress["Calorias"] += calories
        print(f"Dispositivo sincronizado! +{steps} passos e +{calories:.2f} calorias adicionados.")