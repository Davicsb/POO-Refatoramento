import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controller.factory import FitnessComponentFactory
from View.view import FitnessApp

if __name__ == "__main__":
    app = FitnessApp()
    app.run()