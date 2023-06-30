from .models import Singer,Song
from rest_framework import serializers

class SongSerializer(serializers.Serializer):
    class Meta:
        model=Song
        fields=['id','title','singer','duration']

class SingerSerializer(serializers.Serializer):
    song=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Singer
        fields=['id','name','gender','song']
