import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controler.factory import FitnessComponentFactory
from View.view import FitnessApp

if __name__ == "__main__":
    factory = FitnessComponentFactory()
    app = FitnessApp(factory)
    app.run()