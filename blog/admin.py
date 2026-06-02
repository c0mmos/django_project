from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ('title','author','counted_views','status','published_date','created_date')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content')
    ordering = ['-created_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)