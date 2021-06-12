from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import MovieSerializer
from reviews.serializers import ReviewSerializer
from .models import Movie
from random import sample

from movies import serializers

# Create your views here.

# 페이지 대문을 위한 영화 포스터 20개 랜덤추출
@api_view(['GET'])
def main(request):
    poster_base_url = 'https://image.tmdb.org/t/p/w500/'
    poster_urls = []
    movies = sample(get_list_or_404(Movie), 20)
    serializer = MovieSerializer(movies, many=True)
    random_movies = serializer.data
    for random_movie in random_movies:
        movie_src = random_movie.get('poster_path')
        poster_url = poster_base_url + movie_src
        poster_urls.append(poster_url)
    return Response(poster_urls)

# 검색을 위한 전체 영화 데이터 응답
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def search(request):
    movies = get_list_or_404(Movie)
    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)

# 전체 영화 조회 (get), 영화 생성(post)
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    if request.method == 'GET':
        page_number = request.GET.get('p', 1)
        movies = get_list_or_404(Movie)
        paginator = Paginator(movies, 20)
        serializer = MovieSerializer(paginator.page(page_number), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method =='POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 영화 상세 조회 (get), 영화 수정(put), 영화 삭제(delete)
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        movie.delete()
        return Response(f'{movie_pk} : {movie.title} 성공적으로 삭제되었습니다.', status=status.HTTP_204_NO_CONTENT)

# 유저 -> 영화 좋아요
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    context = {}
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        if movie.movie_liked_user.filter(pk=request.user.pk).exists():
            movie.movie_liked_user.remove(request.user)
            context['like'] = False
        else:
            movie.movie_liked_user.add(request.user)
            context['like'] = True
        context['count'] = movie.movie_liked_user.count()
        return Response(context)

    elif request.method == 'GET':
        context['count'] = movie.movie_liked_user.count()
        if request.user.like_movie.filter(pk=movie_pk).exists():
            context['like'] = True
        else:
            context['like'] = False
        return Response(context)

# 유저 -> 영화 봤어요
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_watch(request, movie_pk):
    context = {}
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.movie_watched_user.filter(pk=request.user.pk).exists():
            movie.movie_watched_user.remove(request.user)
            context['watch'] = False
        else:
            movie.movie_watched_user.add(request.user)
            context['watch'] = True
        return Response(context)

    elif request.method == 'GET':
        if request.user.watch_movie.filter(pk=movie_pk).exists():
            context['watch'] = True
        else:
            context['watch'] = False
        return Response(context)

# 영화 리뷰 작성(post)
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 추천 영화 조회 (get)
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommendation(request):
    user = request.user
    if user.watch_movie.count():
        watch_base = get_list_or_404(user.watch_movie)
        promising = set()
        for watch_movie in watch_base:
            watched_users = get_list_or_404(watch_movie.movie_watched_user)
            for w_user in watched_users:
                promising.add(w_user)
        promising = list(promising)
        most_similar_movie = []
        most_unsimilar_cnt = 10000
        for candidate in promising:
            if candidate != user:
                watch_compare = get_list_or_404(candidate.watch_movie)
                compare = list(set(watch_compare) | set(watch_base))
                unsimilar_cnt = len(compare) - len(watch_compare)
                if unsimilar_cnt < most_unsimilar_cnt:
                    most_unsimilar_cnt = unsimilar_cnt
                    most_similar_movie = list(set(watch_compare) - set(watch_base))
        if len(most_similar_movie) > 5:
            recommendation_movie = sample(most_similar_movie, 5)
        elif len(most_similar_movie) == 0:
            recommendation_movie = sample(get_list_or_404(Movie), 5)
        else:
            absent = 5 - len(most_similar_movie)
            recommendation_movie = most_similar_movie + sample(get_list_or_404(Movie), absent)
    else:
        recommendation_movie = sample(get_list_or_404(Movie), 5)
    serializer = MovieSerializer(recommendation_movie, many=True)
    return Response(serializer.data)

# 랜덤
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def random(request):
    movies = get_list_or_404(Movie)
    movie = sample(movies, 1)
    serializer = MovieSerializer(movie[0])
    return Response(serializer.data)