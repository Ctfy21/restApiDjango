from rest_framework.response import Response
from rest_framework import serializers
from .models import Experiment

class ExperimentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    max_recurrence = serializers.IntegerField()
    max_regime = serializers.IntegerField()
    max_box_variety = serializers.IntegerField()
    start_time = serializers.DateField()
    
    def create(self, validated_data):
        return Experiment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.max_recurrence = validated_data.get("max_recurrence", instance.max_recurrence)
        instance.max_regime = validated_data.get("max_regime", instance.max_regime)
        instance.max_box_variety = validated_data.get("max_box_variety", instance.max_box_variety)
        instance.start_time = validated_data.get("start_time", instance.start_time)
        instance.save()
        return instance
    
        
        
        