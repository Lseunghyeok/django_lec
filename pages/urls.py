from django.urls import path
from . import views

urlpatterns = [
  path('', views.mainpage),
  path('company/', views.company),
  path('homepage/', views.homepage),
  path('login/', views.login),
  path('find/', views.find),
  path('custmer/', views.custmer),
  path('membership/', views.membership),
  path('shopping/', views.shopping),
  path('mypage/', views.mypage),
]
