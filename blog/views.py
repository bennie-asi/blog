from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import HttpResponse


def index(request):
    # 查询出所有的文章并根据创建时间排序逆序排序，-（减号）表示逆序
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })
