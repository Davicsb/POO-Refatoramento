import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from View.view import FitnessApp

if __name__ == "__main__":
    app = FitnessApp()
    app.run()