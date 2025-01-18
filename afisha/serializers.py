from .models import Movie, Director, Review
from rest_framework import serializers

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name')

class MovieSerializer(serializers.ModelSerializer):
        directors = DirectorSerializer()
        reviews = ReviewSerializer(many=True)

        class Meta:
            model = Movie
            fields = ("id", "title", "description", "duration", "directors", "rewiews")

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review,
        fields = ("id", "movie", "text")