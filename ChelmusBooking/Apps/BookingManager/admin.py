from django.contrib import admin
from . import models

EMPTY_VALUE = '-empty-'

# Register your models here.

class PostTypeAdmin(admin.ModelAdmin):
    """
        PostType's meta for admin site.
    """
    list_display = ('pk', 'name', 'description', )
    ordering = ['name', ]
    empty_value_display = EMPTY_VALUE
    

class PostAdmin(admin.ModelAdmin):
    """
        Post's meta for admin site.
    """
    list_display = ('pk', 'name', 'post_type', 'description', 'address', 'stars', 'price', 'rating', 'visitors_no', 'posted_on', )
    ordering = ['name', ]
    empty_value_display = EMPTY_VALUE
    
    
# register entries

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.PostType, PostTypeAdmin)
