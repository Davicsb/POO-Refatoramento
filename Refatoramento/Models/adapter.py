# Em algum arquivo base, como interfaces.py
from abc import ABC, abstractmethod

class FitnessComponent(ABC):
    def execute(self):
        self.pre_execute()
        self.run()
        self.post_execute()

    def pre_execute(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def post_execute(self):
        pass


class ShareProgressAdapter(FitnessComponent):
    def __init__(self, app):
        self.app = app

    def run(self):
        self.app.share_progress()

class RecommendationsAdapter(FitnessComponent):
    def __init__(self, app):
        self.app = app

    def run(self):
        self.app.get_recommendations()
        
    def post_execute(self):
        print("Todas as recomendações foram vizualizadas!")

class DataViewer(FitnessComponent):
    def __init__(self, app):
        self.app = app

    def run(self):
        self.app.see_data()
        
    def post_execute(self):
        print("Todos os dados foram vizualizados!")

class ExitHandler(FitnessComponent):
    def pre_execute(self):
        print("Saindo do app...")
    
    def run(self):
        exit()

class GoalSetter(FitnessComponent):
    def __init__(self, activity_tracker):
        self.activity_tracker = activity_tracker

    def run(self):
        self.activity_tracker.set_goals()
        
    def post_execute(self):
        print("Metas definidas com sucesso!")

class DeviceSyncer(FitnessComponent):
    def __init__(self, activity_tracker):
        self.activity_tracker = activity_tracker

    def run(self):
        self.activity_tracker.device_sync()
        
    def post_execute(self):
        print("Dispositivo sincronizado com sucesso!")