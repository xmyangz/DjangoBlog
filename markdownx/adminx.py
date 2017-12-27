#from django.contrib import admin

from .widgets import AdminMarkdownxWidget
from .models import MarkdownxField


#lass MarkdownxModelAdmin(admin.ModelAdmin):
class MarkdownxModelAdmin(object):
    """
    Django admin representation for ``MarkdownxField`` in models.
    
    See **Django Admin** in :doc:`../../example` for additional information.
    """

    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }
