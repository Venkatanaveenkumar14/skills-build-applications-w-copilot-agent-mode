from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate Users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe"},
            {"email": "jane.smith@example.com", "name": "Jane Smith"},
        ]
        user_objects = [User.objects.create(**user) for user in users]

        # Populate Teams
        teams = [
            {"name": "Team Alpha", "description": "The first team"},
            {"name": "Team Beta", "description": "The second team"},
        ]
        team_objects = [Team.objects.create(**team) for team in teams]

        # Populate Activities
        activities = [
            {"activity_id": "A1", "user": user_objects[0], "description": "Running 5km"},
            {"activity_id": "A2", "user": user_objects[1], "description": "Cycling 10km"},
        ]
        activity_objects = [Activity.objects.create(**activity) for activity in activities]

        # Populate Leaderboard
        leaderboards = [
            {"leaderboard_id": "L1", "team": team_objects[0], "score": 100},
            {"leaderboard_id": "L2", "team": team_objects[1], "score": 80},
        ]
        leaderboard_objects = [Leaderboard.objects.create(**leaderboard) for leaderboard in leaderboards]

        # Populate Workouts
        workouts = [
            {"workout_id": "W1", "user": user_objects[0], "details": "Push-ups and sit-ups"},
            {"workout_id": "W2", "user": user_objects[1], "details": "Yoga and stretching"},
        ]
        workout_objects = [Workout.objects.create(**workout) for workout in workouts]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))