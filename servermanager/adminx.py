#from django.contrib import admin

# Register your models here.
from .models import commands
import xadmin

class CommandsAdmin(object):
    list_display = ('title', 'command', 'describe')


xadmin.site.register(commands, CommandsAdmin)
