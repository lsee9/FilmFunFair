from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main), # get, post
    path('<int:post_pk>/', views.detail), # get, put, delete
    path('<int:post_pk>/like/', views.post_like), # like
    path('<int:post_pk>/comment/', views.comment), # post
    path('<int:post_pk>/comment/<int:comment_pk>/', views.comment_delete), # delete
]
