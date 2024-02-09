from .models import Post, User
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'is_active']
    readonly_fields = ['is_active', 'created_at', 'updated_at']


admin.site.register(Post, PostAdmin)
admin.site.register(User)
