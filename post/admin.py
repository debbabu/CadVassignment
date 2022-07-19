from django.contrib import admin

from post.models import *
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Reply)
