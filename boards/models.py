from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="名字")
    description = models.CharField(max_length=100, verbose_name="描述")

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Topic(models.Model):
    subject = models.CharField(max_length=255, verbose_name="主题名称")
    last_updated = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")
    board = models.ForeignKey(Board, related_name="topics", verbose_name="分类")
    starter = models.ForeignKey(User, related_name="topics", verbose_name="创建人")
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "主题"
        verbose_name_plural = verbose_name


class Post(models.Model):
    message = models.TextField(max_length=4000, verbose_name="消息")
    topic = models.ForeignKey(Topic, related_name="posts", verbose_name="主题")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="更新时间")
    created_by = models.ForeignKey(User, related_name="posts", verbose_name="创建作者")
    updated_by = models.ForeignKey(User, null=True, related_name="+", verbose_name="更新作者")

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)

    class Meta:
        verbose_name = "消息"
        verbose_name_plural = verbose_name




