from django.db import models

# Create your models here.
# LIKE_TYPE = (
#     ('like','Like'),
#     ('dislike','Dislike')
# )
class Post(models.Model):
    text = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    @property
    def like_count(self):
        return self.like_posts.filter(post=self.id).count()
    @property
    def dislike_count(self):
        return self.dislike_posts.filter(post=self.id).count()

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='like_posts', unique=True)
    # like_type = models.CharField(max_length=50, choices=LIKE_TYPE, null=True, blank=True,)

class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='dislike_posts', unique=True)

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='reply_posts')
    text = models.TextField()

