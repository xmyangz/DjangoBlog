#from django.contrib import admin

# Register your models here.
from .models import Comment
import xadmin

class CommentAdmin(object):
    list_display = ('id', 'body', 'author', 'article', 'last_mod_time')
    list_display_links = ('id', 'body')
    list_filter = ('author', 'article',)
    exclude = ('created_time', 'last_mod_time')


xadmin.site.register(Comment, CommentAdmin)
