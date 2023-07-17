from django.urls import path
from . import views

urlpatterns = [
  path('', views.mainpage),
  path('company/', views.company),
  path('homepage/', views.homepage),
  path('login/', views.login),
  path('find/', views.find),
  path('customer/', views.customer),
  path('membership/', views.membership),
  path('shopping/', views.shopping),
  path('mypage/', views.mypage),
  path('context/', views.context),
]
