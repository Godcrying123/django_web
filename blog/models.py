from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        {STATUS_NORMAL, 'normal'},
        {STATUS_DELETE, 'delete'},
    )

    name = models.CharField(max_length=50, verbose_name='category name')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    is_nav = models.BooleanField(default=False, verbose_name='is nav')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author',)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created time')

    class Meta:
        verbose_name = verbose_name_plural = 'category'

    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        {STATUS_NORMAL, 'normal'},
        {STATUS_DELETE, 'delete'},
    )

    name = models.CharField(max_length=10, verbose_name='tag name')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created time')

    class Meta:
        verbose_name = verbose_name_plural = 'tag'

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        {STATUS_NORMAL, 'normal'},
        {STATUS_DELETE, 'delete'},
        {STATUS_DRAFT, 'draft'},
    )

    title = models.CharField(max_length=255, verbose_name='title')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='descriptions')
    content = models.TextField(verbose_name='content', help_text='the post must be MarkDown format')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='tag')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created time')

    class Meta:
        verbose_name = verbose_name_plural = 'post'
        ordering = ['-id']
