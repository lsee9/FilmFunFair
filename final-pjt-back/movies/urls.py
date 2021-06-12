from django.urls import path
from . import views

urlpatterns = [
    path('', views.main), # 홈페이지 대문으로 사용할 영화 get
    path('search/', views.search), # 검색을 위한 전체 영화 조회
    path('index/', views.index), # 전체영화조회 get, post
    path('<int:movie_pk>/', views.detail), # 영화 상세 페이지 get, put, delete
    path('<int:movie_pk>/like/', views.movie_like), # 단일 영화 좋아요
    path('<int:movie_pk>/watch/', views.movie_watch), # 단일 영화 봤어요
    path('<int:movie_pk>/review/', views.review_create), # 영화 리뷰 POST
    path('recommendation/', views.recommendation), # 영화추천페이지 get
    path('random/', views.random), # 오늘의 랜덤영화
]
