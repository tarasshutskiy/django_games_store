from django.contrib import admin
from .models import PurchaseHistory, Comment
from django.contrib.auth import get_user_model


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['profile_picture', 'username', ]
    list_display_links = ['username', ]
    search_fields = ['username',]


@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'game',]
    search_fields = ['user', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'game']
    list_display_links = ['user', ]
    search_fields = ['user',]
