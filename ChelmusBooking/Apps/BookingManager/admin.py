from django.contrib import admin

EMPTY_VALUE = '-empty-'

# Register your models here.

class PostTypeAdmin(admin.ModelAdmin):
    """
        PostType's meta for admin site.
    """
    list_display = ('pk', 'name', 'description', )
    ordering = ['name', ]
    empty_value_display = EMPTY_VALUE