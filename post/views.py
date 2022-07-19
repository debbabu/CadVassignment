from django.shortcuts import render
from post.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from post.serializers import *

class PostView(ModelViewSet):
    serializer_class = PostSerializer
    http_method_names = ['get', 'post',]

    def list(self, request):
        posts = Post.objects.all()
        serializers_var = self.serializer_class(posts, many=True)
        return Response(serializers_var.data)

class LikeView(ModelViewSet):
    serializer_class = LikeSerializer
    http_method_names = ['get', 'post',]

class DislikeView(ModelViewSet):
    serializer_class = DislikeSerializer
    http_method_names = ['get', 'post',]

class ReplyView(ModelViewSet):
    serializer_class = ReplySerializer
    http_method_names = ['get', 'post',]