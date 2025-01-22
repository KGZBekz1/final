from itertools import product
from wsgiref.validate import validator
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MovieValiditySerializer


@api_view(http_method_names=['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def movie_detail_view(request, id):
    movie = get_object_or_404(Movie, id=id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


def post(self, request, *args, **kwargs):
    validator = MovieValiditySerializer(data=request.data)
    if not validator.is_valid():
        return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
    title = validator.validated_data('title')
    description = validator.validated_data('description')
    duration = validator.validated_data('duration')
    director = validator.validated_data('director')
    movie = Movie.objects.create(title=title, description=description, duration=duration, director=director)
    movie.save()
    return Response({'id': movie.id}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        product_detail = self.get_object()
        validator = MovieValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        product_detail.title = validator.validated_data('title')
        product_detail.description = validator.validated_data('description')
        product_detail.duration = validator.validated_data('duration')
        product_detail.director = validator.validated_data('director')
        product_detail.save()
        return Response(product_detail).data, status.HTTP_200_OK

    def post(self, request, *args, **kwargs):
        validator = MovieValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        text = validator.validated_data('text')
        movie = validator.validated_data('movie')
        stars = validator.validated_data('stars')
        review = validator.validated_data('review')
        review.save()
        return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)


    def put(self, request, *args, **kwargs):
        review_detail = self.get_object()
        validator = MovieValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        review_detail.text = validator.validated_data('text')
        review_detail.movie = validator.validated_data('movie')
        review_detail.stars = validator.validated_data('stars')
        review_detail.save()
        return Response(ReviewSerializer(review_detail).data, status=status.HTTP_200_OK)