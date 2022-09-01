from django.contrib import admin
from .models import Contact

# 注册到管理后台，方便管理
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'created_time']
    fields = ['name', 'email', 'subject', 'message']


admin.site.register(Contact, ContactAdmin)
