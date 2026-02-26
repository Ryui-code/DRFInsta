from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'followings', FollowViewSet, basename='follow')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'post_contents', PostContentViewSet, basename='post_content')
router.register(r'post_likes', PostLikeViewSet, basename='post_like')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'comment_likes', CommentLikeViewSet, basename='comment_like')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls))
]