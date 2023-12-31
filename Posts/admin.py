from django.contrib import admin

from .models import post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date']
    search_fields = ["title", 'content']
    list_filter = ["author", "publish_date"]



admin.site.register(post,PostAdmin) 