from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup), # post
    path('login/', obtain_jwt_token), # 로그인 기능 나머지는 프론트에서
    path('mypage/', views.mypage), # get
    path('mypage/mypost/', views.mypost), # get, 내가쓴 리뷰와 관련된 모든 정보
]
