
from wsgiref import validate
from django.forms import ValidationError
from rest_framework import serializers
from video.models import video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields ='__all__'
        
        
    def validate(self, data):
        if data['title']<10:
            raise serializers.ValidationError({'error':"exceed"})
        
        return data