from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'post_title',
        'post_author',
        'post_date_posted',
    )

    ordering = ('-post_date_posted',)

admin.site.register(Post, PostAdmin)
