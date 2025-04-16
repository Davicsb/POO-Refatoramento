# Em algum arquivo base, como interfaces.py
from abc import ABC, abstractmethod

class FitnessComponent(ABC):
    @abstractmethod
    def execute(self):
        pass

class ShareProgressAdapter(FitnessComponent):
    def __init__(self, app):
        self.app = app

    def execute(self):
        self.app.share_progress()

class RecommendationsAdapter(FitnessComponent):
    def __init__(self, app):
        self.app = app

    def execute(self):
        self.app.get_recommendations()

class DataViewer(FitnessComponent):
    def __init__(self, app):
        self.app = app

    def execute(self):
        self.app.see_data()

class ExitHandler(FitnessComponent):
    def execute(self):
        print("Saindo do app...")
        exit()

class GoalSetter(FitnessComponent):
    def __init__(self, activity_tracker):
        self.activity_tracker = activity_tracker

    def execute(self):
        self.activity_tracker.set_goals()

class DeviceSyncer(FitnessComponent):
    def __init__(self, activity_tracker):
        self.activity_tracker = activity_tracker

    def execute(self):
        self.activity_tracker.device_sync()
