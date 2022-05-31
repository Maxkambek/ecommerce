from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', )


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
