#from django.contrib import admin

# Register your models here.
from .models import OAuthUser
import xadmin

class OAuthUserAdmin(object):
    list_display = ('id', 'author', 'nikename', 'type', 'picture', 'email',)
    list_display_links = ('id', 'nikename')
    list_filter = ('author', 'type',)


xadmin.site.register(OAuthUser, OAuthUserAdmin)
