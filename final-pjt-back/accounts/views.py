from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserSerializer

from .models import User
from movies.models import Movie
from movies.serializers import MovieSerializer
from communities.models import Post


# Create your views here.

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def mypage(request):
    user = request.user
    # 내가 본 영화 리스트
    my_movie_watch_list = list(user.watch_movie.all().values())
    # 내가 좋아요한 영화 리스트
    my_movie_like_list = list(user.like_movie.all().values())

    # 내가 작성한 리뷰 데이터
    #.movie로 어떤 영화인지 접근 가능 -> 리뷰를 작성한 영화 데이터
    my_review_list = list(user.user_review.all().values())


    # 내가 쓴 게시글 데이터
    my_posts= user.user_post.all().values()
    my_post = []
    for post_info in my_posts:
        # 게시글 정보
        post = get_object_or_404(Post, pk=post_info['id'])
        # 댓글 갯수
        post_info['comment_count'] = post.post_comment.count()
        # 좋아요 개수
        post_info['like_count'] = post.post_liked_user.count()
        my_post.append(post_info)

    context = {
        'user_name' : user.username,
        'my_movie_watch_list' : my_movie_watch_list,
        'my_movie_like_list' : my_movie_like_list,
        'my_review_list' : my_review_list,
        'my_post' : my_post,
    }
    return JsonResponse(context, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def mypost(request):
    context = {}
    if request.method == 'GET':
        my_movies = []
        my_review_movie = request.user.user_review.all().values('movie_id')
        print(my_review_movie)
        for movie in my_review_movie:
            my_movie = get_object_or_404(Movie, pk=movie['movie_id'])
            movie_info = MovieSerializer(my_movie).data
            # 해당 영화를 좋아요한 사람 수
            movie_info['count'] = my_movie.movie_liked_user.count()

            # 현재 유저가 좋아한 영화에 해당 영화가 있는 경우
            if request.user.like_movie.filter(pk=movie['movie_id']).exists():
                movie_info['like'] = True
            # 영화가 없는 경우
            else:
                movie_info['like'] = False
            
            my_movies.append(movie_info)
        context = {
            'my_movies': my_movies,
        }
        return Response(context)
