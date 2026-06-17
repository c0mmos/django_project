from django.contrib import admin
from base_site.models import contact, NewsLetter
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ['name', 'email', 'created_date']
    list_filter = ('email',)
    search_fields = ('name', 'subject', 'message')
    ordering = ["-created_date"]
    
admin.site.register(NewsLetter)
admin.site.register(contact, ContactAdmin)