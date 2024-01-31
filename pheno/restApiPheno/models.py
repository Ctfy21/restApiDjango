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
    
class Regime(models.Model):
    title = models.CharField(max_length=200)
    temperature = models.FloatField()
    
    def __str__(self):
        return self.title   
    
class Recurrence(models.Model):
    title

    
