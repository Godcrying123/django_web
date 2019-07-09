from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from django.contrib.auth import get_permission_codename
from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from myidea.custom_site import custom_site
from myidea.base_admin import BaseOwnerAdmin
# Register your models here.


class PostInline(admin.TabularInline): #different StackedInline Style
    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline]
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time', 'post_count')
    fields = ('name', 'status', 'owner', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = 'post_count'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status', 'owner')


class CategoryOwnerFilter(admin.SimpleListFilter):
    """customized filter only shows the current user category"""

    title = 'category filter'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


# PERMISSION_API = "http://permission.sso.com/has_perm?user={}&perm_code={}"

@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    # form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'owner', 'operator'
    ]
    list_display_links = []

    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    #edit the page
    # save_on_top = True

    exclude = ('owner',)

    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    fieldsets = (
        ('basic configs', {
           'description': 'basic config descriptions', 'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('content', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('extra info', {
            # 'classes': ('collapse',),
            'fields': ('tag',),
        }),
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">Edit</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id, ))
        )
    operator.short_description = 'operate'

    class Media:
        css = {
            'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css', ),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']