from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    like_counts = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.description + ' - ' + str(self.user)

class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def update_likes(self):
        self.post.like_counts = self.liked_by.count()
        self.save()

class FollowUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_by', editable=False)
    user_following = models.ManyToManyField(User)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)