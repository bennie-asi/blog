from django.contrib import admin

from blog.models import Post, Category, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # 控制Post列表页展示的字段
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # 控制表单页展示的字段
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    # 重写ModelAdmin的save_model方法，将从request对象中的user放进去
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
