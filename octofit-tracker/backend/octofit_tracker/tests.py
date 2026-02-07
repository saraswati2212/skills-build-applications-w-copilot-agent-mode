from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='testuser', activity_type='run', duration=30)
        self.assertEqual(activity.user, 'testuser')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user='testuser', points=50)
        self.assertEqual(lb.points, 50)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups')
        self.assertEqual(workout.name, 'Pushups')
