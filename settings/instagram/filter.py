from django_filters import FilterSet
from .models import Post, UserProfile

class PostFilterSet(FilterSet):
    class Meta:
        model = Post
        fields = [
            'user',
            'hashtag'
        ]

class UserFilterSet(FilterSet):
    class Meta:
        model = UserProfile
        fields = [
            'username'
        ]