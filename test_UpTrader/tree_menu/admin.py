from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')
    list_filter = ('name',)
    search_fields = ('name', 'url')
    ordering = ('name', 'id')


admin.site.register(MenuItem, MenuItemAdmin)
