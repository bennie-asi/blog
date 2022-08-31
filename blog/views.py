import re
import markdown
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from markdown.extensions.toc import TocExtension
from pure_pagination import PaginationMixin

from .models import Post, Category, Tag


# Create your views here.

# 类视图
class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    #     开启分页
    paginate_by = 6


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class ArchiveView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        return (
            super()
            .get_queryset()
            .filter(created_time__year=year, created_time__month=month)
        )


class TagView(IndexView):

    def get_queryset(self):
        t = get_object_or_404(Tag, pk=self.kwargs.get("pk"))
        return super().get_queryset().filter(tags=t)


# 记得在顶部导入 DetailView
class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super().get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            # 记得在顶部引入 TocExtension 和 slugify
            TocExtension(slugify=slugify),
        ])
        post.body = md.convert(post.body)

        m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
        post.toc = m.group(1) if m is not None else ''

        return post
# 视图函数
# '''文章列表'''
#
#
# def index(request):
#     # 查询出所有的文章并根据创建时间排序逆序排序，-（减号）表示逆序
#     post_list = Post.objects.all()
#     return render(request, 'blog/index.html', context={
#         'post_list': post_list
#     })
#
#
# '''文章详情'''
#
#
# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     # 阅读量+1
#     post.increase_views()
#     # 添加Markdown语法拓展，包含额外拓展，语法高亮和自动生成目录
#     md = markdown.Markdown(extensions=[
#         'markdown.extensions.extra',
#         'markdown.extensions.codehilite',
#         # 'markdown.extensions.fenced_code',
#         # 'markdown.extensions.toc',
#         TocExtension(slugify=slugify),
#     ])
#     post.body = md.convert(post.body)
#     #  post 实例本身是没有 toc 属性的，给它动态添加了 toc 属性
#     # post.toc = md.toc
#     m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
#     post.toc = m.group(1) if m is not None else ''
#     return render(request, 'blog/detail.html', context={'post': post})
#
#
# '''归档'''
#
#
# def archive(request, year, month):
#     post_list = Post.objects.filter(created_time__year=year,
#                                     created_time__month=month
#                                     )
#     return render(request, 'blog/index.html', context={'post_list': post_list})
#
#
# '''分类，通过传入分类的id值来从数据库中获取值'''
#
#
# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate)
#     return render(request, 'blog/index.html', context={'post_list': post_list})
#
#
# '''标签'''
#
#
# def tag(request, pk):
#     t = get_object_or_404(Tag, pk=pk)
#     post_list = Post.objects.filter(tags=t)
#     return render(request, 'blog/index.html', context={'post_list': post_list})
