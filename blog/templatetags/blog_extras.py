from django import template
from django.db.models import Count

from ..models import Post, Category, Tag

register = template.Library()

'''编写模板标签函数'''


# 最新文章模板标签 takes_context=True表示传入父模板
@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }


# 归档文章模板标签 按月份进行降序归档
@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }


# 分类模板标签
@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.annotate(num_posts=Count('post'))
    return {
        'category_list': category_list,
    }


# 标签云模板标签
@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    tag_list = Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'tag_list': tag_list,
    }
