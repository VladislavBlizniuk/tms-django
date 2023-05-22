from django.contrib import admin

from .models import Article


# admin.site.register(Article)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'author', 'like_count']}),
        ('Content', {'fields': ['text']})
    ]
    readonly_fields = ['like_count', 'is_popular']
    search_fields = ['title', 'author', 'text']
    list_display = ['title', 'author', 'like_count', 'is_popular']
    list_filter = ['title', 'author', 'like_count']