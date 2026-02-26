from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *
import os
from django.conf import settings
import joblib

model_path = os.path.join(settings.BASE_DIR, 'naive_model.pkl')
joblib.load(model_path)

vector_path = os.path.join(settings.BASE_DIR, 'vector.pkl')
joblib.load(vector_path)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'avatar', 'bio', 'hashtag', 'link', 'status', 'registered_date')

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("Invalid credentials.")
        attrs["user"] = user
        return attrs

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"

    def validate(self, attrs):
        if attrs['follower'] == attrs['following']:
            raise serializers.ValidationError("U can not subscribe to yourself.")
        return attrs

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = "__all__"

class PostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostContent
        fields = "__all__"

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

    def validate(self, attrs):
        if PostLike.objects.filter(post=attrs['post'], user=attrs['user']).exists():
            raise serializers.ValidationError("U are already liked it.")
        return attrs

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = "__all__"

class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = "__all__"

    def validate(self, attrs):
        if CommentLike.objects.filter(comment=attrs['comment'], user=attrs['user']).exists():
            raise serializers.ValidationError("Like is already exists.")
        return attrs