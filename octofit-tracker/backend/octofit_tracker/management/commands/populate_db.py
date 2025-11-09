from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel')
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='marvel')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='dc')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='dc')

        # Activities
        Activity.objects.create(user=ironman, type='run', duration=30, date='2025-11-01')
        Activity.objects.create(user=captain, type='cycle', duration=45, date='2025-11-02')
        Activity.objects.create(user=batman, type='swim', duration=60, date='2025-11-03')
        Activity.objects.create(user=superman, type='fly', duration=120, date='2025-11-04')

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=180)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups', suggested_for='marvel')
        Workout.objects.create(name='Flight Training', description='Practice flying', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
