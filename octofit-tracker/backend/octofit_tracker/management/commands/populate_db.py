from django.core.management.base import BaseCommand
from django.db import connection

USERS = [
    {"name": "Clark Kent", "email": "superman@dc.com", "team": "DC"},
    {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "DC"},
    {"name": "Diana Prince", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Steve Rogers", "email": "captainamerica@marvel.com", "team": "Marvel"},
    {"name": "Peter Parker", "email": "spiderman@marvel.com", "team": "Marvel"},
]

TEAMS = [
    {"name": "Marvel"},
    {"name": "DC"},
]

ACTIVITIES = [
    {"user": "superman@dc.com", "activity": "Flying", "duration": 60},
    {"user": "batman@dc.com", "activity": "Martial Arts", "duration": 45},
    {"user": "wonderwoman@dc.com", "activity": "Lasso Training", "duration": 30},
    {"user": "ironman@marvel.com", "activity": "Suit Test", "duration": 50},
    {"user": "captainamerica@marvel.com", "activity": "Shield Throw", "duration": 40},
    {"user": "spiderman@marvel.com", "activity": "Web Swing", "duration": 35},
]

LEADERBOARD = [
    {"team": "Marvel", "points": 125},
    {"team": "DC", "points": 135},
]

WORKOUTS = [
    {"name": "Strength Training", "suggested_for": "DC"},
    {"name": "Agility Drills", "suggested_for": "Marvel"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = connection.cursor().db_conn.client[connection.settings_dict['NAME']]
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)
        db.users.create_index([("email", 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
