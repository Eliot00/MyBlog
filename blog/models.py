from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)               # 博客标题
    category = models.CharField(max_length=50, blank=True) # 博客标签
    body = models.TextField()                              # 博客正文
    timestamp = models.DateTimeField(auto_now_add=True)    # 创建时间

    def __str__(self):
        return self.title