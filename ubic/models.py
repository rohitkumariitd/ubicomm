from django.db import models
import uuid

class User(models.Model):
    first_name = models.CharField(max_length=10)
    def __str__(self):
        return self.first_name

class Ubic(models.Model):
    name = models.CharField(max_length=100)
    image_link = models.URLField()
    description = models.TextField()
    duration = models.PositiveSmallIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    TYPE = (
        ('SS', 'session'),
        ('SR', 'series'),
    )
    type = models.CharField(max_length=2, choices=TYPE, default='SS')
    user = models.ForeignKey(User)
    def __str__(self):
        return self.name

class UbicInstance(models.Model):
    ubic = models.ForeignKey(Ubic)
    instance_index = models.PositiveIntegerField()
    start_date = models.DateField()
    updated_description = models.TextField()
    price = models.PositiveIntegerField()
    registrations = models.ManyToManyField(User)
    def __str__(self):
        return str(self.instance_index)

class WeeklySchedule(models.Model):
    ubic_instance = models.ForeignKey(UbicInstance)
    week_index = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    image_link = models.URLField()
    description = models.TextField()
    def __str__(self):
        return "week " + str(self.week_index) + " instance " + str(self.ubic_instance.instance_index)

class Webinar(models.Model):
    week = models.ForeignKey(WeeklySchedule)
    title = models.CharField(max_length=50)
    time = models.DateTimeField()
    def __str__(self):
        return self.title

class Resource(models.Model):
    week = models.ForeignKey(WeeklySchedule)
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Video(models.Model):
    week = models.ForeignKey(WeeklySchedule)
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
