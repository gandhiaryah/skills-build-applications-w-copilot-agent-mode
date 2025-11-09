from djongo import models

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'team'

class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    class Meta:
        db_table = 'user'

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='_id')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    date = models.DateField()
    class Meta:
        db_table = 'activity'

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, to_field='_id')
    points = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
    class Meta:
        db_table = 'workout'
