from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        {STATUS_NORMAL, 'normal'},
        {STATUS_DELETE, 'delete'},
    )

    title = models.CharField(max_length=50, verbose_name='title')
    href = models.URLField(verbose_name='link')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name='weight',
                                         help_text='weight order from high to low')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created time')

    class Meta:
        verbose_name = verbose_name_plural = 'Link'


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        {STATUS_SHOW, 'show'},
        {STATUS_HIDE, 'hide'},
    )
    SIDE_TYPE = (
        {1, 'HTML'},
        {2, 'Latest Posts'},
        {3, 'Hottest Posts'},
        {4, 'Latest Comments'},
    )
    title = models.CharField(max_length=50, verbose_name='title')
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name='display type')
    content = models.CharField(max_length=500, blank=True, verbose_name='post')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name='status')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created time')

    class Meta:
        verbose_name = verbose_name_plural = 'side bar'
