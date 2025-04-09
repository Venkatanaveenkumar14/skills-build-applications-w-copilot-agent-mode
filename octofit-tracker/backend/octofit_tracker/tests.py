from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelsTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")

    def test_team_creation(self):
        team = Team.objects.create(name="Team A", description="A test team")
        self.assertEqual(team.name, "Team A")