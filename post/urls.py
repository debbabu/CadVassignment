from django.urls import path, include
from post import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post',views.PostView, basename='post')
router.register('like',views.LikeView, basename='like')
router.register('dislike',views.DislikeView, basename='dislike')
router.register('reply',views.ReplyView, basename='reply')
urlpatterns = []
urlpatterns += router.urls

