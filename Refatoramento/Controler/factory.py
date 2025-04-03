from Controler.workout_manager import WorkoutManager
from Controler.goal_manager import GoalManager
from Controler.feedback_manager import FeedbackManager
from Controler.tutorial_manager import TutorialManager
from Controler.forum_manager import ForumManager
from Models.tracker import ActivityTracker
from Models.tracker import NutritionTracker
from Models.devicesync import DeviceSync

class FitnessComponentFactory:
    def create_workout_manager(self):
        return WorkoutManager()

    def create_activity_tracker(self):
        return ActivityTracker()

    def create_nutrition_tracker(self):
        return NutritionTracker()

    def create_goal_manager(self):
        return GoalManager()

    def create_device_sync(self, progress):
        return DeviceSync(progress)

    def create_feedback_manager(self):
        return FeedbackManager()

    def create_tutorial_manager(self):
        return TutorialManager()

    def create_forum_manager(self):
        return ForumManager()