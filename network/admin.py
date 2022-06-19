from django.contrib import admin
from .models import User, Post, LikePost, FollowUser

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowUser)

