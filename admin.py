
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Настройка отображения модели Post в админ-панели"""
    list_display = ('id', 'text', 'pub_date', 'slug')
    list_display_links = ('id', 'text')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    prepopulated_fields = {'slug': ('text',)}