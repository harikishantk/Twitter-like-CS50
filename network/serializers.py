from rest_framework import serializers
from .models import User, Post, LikePost, FollowUser

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'description', 'created_on', 'updated_on', 'like_counts')

class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = ('id', 'post', 'liked_by', 'created_on', 'updated_on')

class FollowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUser
        fields = ('id', 'user', 'user_following', 'created_on', 'updated_on')