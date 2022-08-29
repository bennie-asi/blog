from django.urls import path

from . import views

# 函数命名空间,方便不同应用来寻找对应的URL，找到对应的视图函数
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
]
