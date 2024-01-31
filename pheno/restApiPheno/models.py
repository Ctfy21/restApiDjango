from django.db import models

class Box(models.Model):
    title = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Variety(models.Model):
    title = models.CharField(max_length=200)
    sequence_number = models.IntegerField(null=True)
    
    def __str__(self):
        return self.title 
    
class CurrentValues(models.Model):
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now = True)
    variety = models.ForeignKey('Variety', on_delete=models.PROTECT, null = False)
    box = models.ForeignKey('Box', on_delete=models.PROTECT, null = False)
    recurrence = models.PositiveSmallIntegerField(max_value=100)
    regime = models.FloatField()
    all_plants = models.PositiveSmallIntegerField(max_value=30)
    live_plants = models.PositiveSmallIntegerField(max_value=30)
    grown_plants_value = models.PositiveSmallIntegerField(min_value=0, max_value=9)
    live_plants_percent = models.FloatField()

    def __str__(self):
        return self.time_create

class Experiment(models.Model):
     

    
