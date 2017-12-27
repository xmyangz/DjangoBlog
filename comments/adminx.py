#from django.contrib import admin

# Register your models here.
from .models import Comment
import xadmin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

class CommentAdmin(object):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    list_display = ('id', 'body', 'author', 'article', 'last_mod_time')
    list_display_links = ('id', 'body')
    list_filter = ('author', 'article',)
    exclude = ('created_time', 'last_mod_time')


xadmin.site.register(Comment, CommentAdmin)
