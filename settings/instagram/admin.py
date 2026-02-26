from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(UserProfile)
class UserAdmin(UserAdmin):
    fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'avatar', 'hashtag', 'link', 'bio', 'email', 'status', 'registered_date'
            ),
        }),
    ]
    readonly_fields = ['registered_date']

admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(PostContent)
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(CommentLike)