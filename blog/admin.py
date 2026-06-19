from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    list_display = ('title','author','counted_views','status','published_date','created_date')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content')
    ordering = ['-created_date']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ('name','email','subject','approved','created_date')
    list_filter = ('name', 'post')
    search_fields = ('name', 'subject')
    ordering = ['-created_date']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)