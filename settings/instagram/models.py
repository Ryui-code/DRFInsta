from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    hashtag = models.CharField(null=True, blank=True, max_length=100)
    link = models.URLField(null=True, blank=True)
    status = models.CharField(choices=[('Simple', 'Simple'), ('Pro', 'Pro')])
    registered_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'@{self.username}'

class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='followers', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followings')

    def __str__(self):
        return f'{self.follower.username} > {self.following.username}'

    class Meta:
        unique_together = ('follower', 'following')

class Post(models.Model):
    description = models.TextField(null=True, blank=True)
    hashtag = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.description[:10]} ({self.created_date})'

class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.FileField(upload_to='posts/')

    def __str__(self):
        return self.post.id

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.post.id} - {self.like}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.id}: {self.user.username} - {self.comment[:30]}'

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('comment', 'user')

    def __str__(self):
        return f'{self.comment.id} - {self.like}'

class Chat(models.Model):
    chats = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    texted = models.DateTimeField(auto_now_add=True)