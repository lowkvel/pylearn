from django.contrib import admin

from .models import Comment
from typeidea.custom_admin_site import custom_admin_site
from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.
@admin.register(Comment, site=custom_admin_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'owner', 'created_time')
    fields = ('target', 'nickname', 'content', 'website')


