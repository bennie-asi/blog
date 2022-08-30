from django.urls import path

from . import views

# 函数命名空间,方便不同应用来寻找对应的URL，找到对应的视图函数
app_name = 'blog'
urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.IndexView.as_view(),name='index'),
    # 文章详情
    # path('posts/<int:pk>/', views.detail, name='detail'),
    path('posts/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    # 文章日期访问文章
    # path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(),name='archive'),
    # 文章分类访问文章
    # path('categories/<int:pk>/', views.category, name='category'),
    path('categories/<int:pk>/', views.CategoryView.as_view(),name='category'),
    # 文章标签访问文章
    # path('tags/<int:pk>/', views.tag, name='tag'),
    path('tags/<int:pk>/', views.TagView.as_view(),name='tag'),
]
