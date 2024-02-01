from django.db import models

class Box(models.Model):
    title = models.IntegerField()
    
    def __str__(self):
        return self.title

class Regime(models.Model):
    title = models.CharField(max_length=100)
    live_plants_percent_regime = models.FloatField()
    
    def __str__(self):
        return self.title

class Variety(models.Model):
    title = models.CharField(max_length=200)
    sequence_number = models.IntegerField(null=True)
    is_templated = models.BooleanField(default=False)
    sequence_box_number = models.PositiveSmallIntegerField()
    relative_template_percent = models.FloatField()
    score = models.PositiveSmallIntegerField()
    additional_info = models.TextField(blank=True)
    
    def __str__(self):
        return self.title 
    
class CurrentValues(models.Model):
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now = True)
    variety = models.ForeignKey('Variety', on_delete=models.PROTECT, null = False)
    box = models.ForeignKey('Box', on_delete=models.PROTECT, null = False)
    recurrence = models.PositiveSmallIntegerField()
    regime = models.ForeignKey('Regime', on_delete=models.PROTECT, null = False)
    all_plants = models.PositiveSmallIntegerField()
    live_plants = models.PositiveSmallIntegerField()
    grown_plants_value = models.PositiveSmallIntegerField()
    live_plants_percent = models.FloatField()
    experiment = models.ForeignKey('Experiment', on_delete=models.PROTECT, null = False)
    
    def __str__(self):
        return self.time_create

class Experiment(models.Model):
    title = models.CharField(max_length=200)
    max_recurrence = models.PositiveSmallIntegerField()
    max_regime = models.PositiveSmallIntegerField()
    max_box_variety = models.PositiveSmallIntegerField()
     
    def __str__(self):
        return self.title 
    
