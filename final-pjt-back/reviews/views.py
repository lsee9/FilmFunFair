from django.db.models.deletion import SET_DEFAULT
from rest_framework.fields import ReadOnlyField
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse

from .models import Review
from movies.models import Movie
from .serializers import ReviewSerializer
from reviews import serializers


# Create your views here.

# 전체 리뷰 조회(get)
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def main(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        reviews = movie.movie_review.all()
        avg_star = 0
        if len(reviews):
            for review in reviews:
                avg_star += int(review.star)
            avg_star = round((avg_star / len(reviews)), 2)
        serializer = ReviewSerializer(reviews, many=True)
        data = {   
            'avg_star' : avg_star,
            'reviews' : serializer.data 
        }
        return Response(data, status=status.HTTP_200_OK)
    

# 리뷰 수정(put), 리뷰 삭제(delete), 특정 리뷰 조회(get)
@api_view(['PUT', 'DELETE', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, review_pk, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.movie_review.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        review.delete()
        data = {
            'data': f'review {review_pk}번이 삭제되었습니다'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

# 유저 -> 리뷰 좋아요
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_like(request, review_pk, movie_pk):
    if request.method == 'POST':
        context = {}
        review = get_object_or_404(Review, pk=review_pk)
        if review.review_liked_user.filter(pk=request.user.pk).exists():
            review.review_liked_user.remove(request.user)
            context['like'] = False
        else:
            review.review_liked_user.add(request.user)
            context['like'] = True
        context['count'] = review.review_liked_user.count()
        return Response(context)

