from rest_framework import serializers
from post.models import *

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id','post','text')
        # extra_kwargs = {'post': {'required': False}}

class PostSerializer(serializers.ModelSerializer):
    reply_posts = ReplySerializer(allow_null=True, many=True, required=False)
    like_count = serializers.ReadOnlyField()
    dislike_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id','text','like_count','dislike_count','reply_posts','created_on')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id','post',)

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ('id','post',)