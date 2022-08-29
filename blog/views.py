import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
from django.http import HttpResponse


def index(request):
    # 查询出所有的文章并根据创建时间排序逆序排序，-（减号）表示逆序
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 添加Markdown语法拓展，包含额外拓展，语法高亮和自动生成目录
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 'markdown.extensions.fenced_code',
        'markdown.extensions.toc',
    ])

    return render(request, 'blog/detail.html', context={'post': post})
