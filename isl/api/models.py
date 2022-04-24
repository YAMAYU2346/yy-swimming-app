# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=10)
    match = models.ForeignKey('Match', models.DO_NOTHING)
    classa = models.CharField(db_column='classA', max_length=10)  # Field name made lowercase.
    team_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'athlete'


class Event(models.Model):
    match = models.ForeignKey('Match', models.DO_NOTHING)
    event_number = models.IntegerField()
    distance = models.CharField(max_length=10)
    style = models.CharField(max_length=10)
    class_1 = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'event'


class Match(models.Model):
    name = models.CharField(max_length=200)
    team_num = models.SmallIntegerField()
    entry_url = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'match'


class Result(models.Model):
    event = models.ForeignKey(Event, models.DO_NOTHING)
    athlete = models.ForeignKey(Athlete, models.DO_NOTHING)
    lane = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result'


class Team(models.Model):
    match = models.ForeignKey(Match, models.DO_NOTHING)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'
