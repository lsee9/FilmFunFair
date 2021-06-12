from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/movie/', views.main), # 전체 리뷰 get
    path('<int:review_pk>/movie/<int:movie_pk>/', views.detail), # put, delete, get
    path('<int:review_pk>/movie/<int:movie_pk>/like/', views.review_like), # like
]
