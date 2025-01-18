from django.shortcuts import render
from .models import Movie,Director,Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer
from rest_fromework import generics


class DirectorListAPIView(generics.ListcreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailAPIView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

class MovieListAPIView(generics.ListcreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'