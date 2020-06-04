from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'author', 'title', 'created_date', 'published_date')
    raw_id_fields = ('author',)
    pass
