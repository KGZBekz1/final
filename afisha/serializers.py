from .models import Movie, Director, Review
from rest_framework import serializers


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ("id", "name", "movie_count")

    def get_movie_count(self, director):
        return director.movie_count


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review,
        fields = ("id", "text", "movie", "stars",)


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    directors = DirectorSerializer()
    reviews = ReviewSerializer(many=True)


class Meta:
    model = Movie
    fields = ("id", "title", "description", "duration", "directors", "reviews", "average_rating")


def get_average_rating(self, movie):
    reviews = movie.reviews.all()
    if reviews:
        sum_reviews = sum([reviews.start for review in reviews])
        average = sum_reviews / len(reviews)
        return average
    return None