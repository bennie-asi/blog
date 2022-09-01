from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    name = models.CharField("名称", max_length=50)
    email = models.EmailField("邮箱", blank=True)
    subject = models.CharField("主题", max_length=80, blank=True)
    created_time = models.DateTimeField("时间", default=timezone.now)
    message = models.TextField("信息")

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return '{}: {}'.format(self.name, self.message[:20])
