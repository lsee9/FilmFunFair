from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Post, Comment
from .serializers import (
    PostListSerializer,
    PostSerializer,
    CommentSerializer,
)


# Create your views here.

# 전체 게시글 조회(get), 게시글 작성(post)
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def main(request):
    if request.method == 'GET':
        page_number = request.GET.get('p', 1)
        posts = get_list_or_404(Post)
        posts = Post.objects.order_by('-pk')
        paginator = Paginator(posts, 20)
        serializer = PostListSerializer(paginator.page(page_number), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 게시글 상세 페이지 조회(get), 게시글 수정(put), 게시글 삭제(delete) 
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        post.delete()
        data = {
            'data': f'post {post_pk}번이 삭제되었습니다'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

# 유저 -> 게시글 좋아요
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def post_like(request, post_pk):
    context = {}
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        if post.post_liked_user.filter(pk=request.user.pk).exists():
            post.post_liked_user.remove(request.user)
            context['like'] = False
        else:
            post.post_liked_user.add(request.user)
            context['like'] = True
        context['count'] = post.post_liked_user.count()

        return Response(context)

    # 게시글 정보 요청
    elif request.method == 'GET':
        context['count'] = post.post_liked_user.count()
        if request.user.like_post.filter(pk=post_pk).exists():
            context['like'] = True
        else:
            context['like'] = False
        return Response(context)

# 댓글 생성(post)
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# comment 삭제
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        data = {
            'data': f'comment {comment_pk}번이 삭제되었습니다'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
