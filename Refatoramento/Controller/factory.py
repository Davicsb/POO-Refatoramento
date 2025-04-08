from Controller.workout_manager import WorkoutManager
from Controller.feedback_manager import FeedbackManager
from Controller.tutorial_manager import TutorialManager
from Controller.forum_manager import ForumManager
from Models.tracker import ActivityTracker
from Models.tracker import NutritionTracker

class FitnessComponentFactory:
    def create_workout_manager(self):
        return WorkoutManager()

    def create_activity_tracker(self):
        return ActivityTracker()

    def create_nutrition_tracker(self):
        return NutritionTracker()

    def create_feedback_manager(self):
        return FeedbackManager()

    def create_tutorial_manager(self):
        return TutorialManager()

    def create_forum_manager(self):
        return ForumManager()