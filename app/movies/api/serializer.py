from rest_framework import serializers
from .models import *

class ActorSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True, source='Act_Movies')
    class Meta:
        model = Actor
        fields = ['id', 'name', 'age', 'gender', 'movies']
        depth=1

class DirectorSerializer(serializers.ModelSerializer):
    movies=serializers.StringRelatedField(many=True, source='Dir_Movies')
    class Meta:
        model = Director
        fields = ['id', 'name', 'nationality', 'Gender', 'dob', 'bio', 'movies']
        depth=1

class MovieSerializer(serializers.ModelSerializer):
    director_name = serializers.ReadOnlyField(source='Movie_Director.name')
    Actors_names = serializers.StringRelatedField(many=True, source='actors')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'director_name', 'Actors_names']
