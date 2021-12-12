from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.html import format_html
from imagekit.admin import AdminThumbnail

class AdminImageWidget(AdminFileWidget):
    """Admin widget for showing clickable thumbnail of Image file fields"""

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and getattr(value, 'url', None):
            html = format_html('<a href="{0}" target="_blank"><img src="{0}" alt="{1}" width="150" height="150" style="object-fit: contain;"/></a>', value.url, str(value)) + html
        return html

# Register your models here.
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import balloon, balloon_type, balloon_sub_type


class balloon_type_admin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name_cn", "name_en", "order")

admin.site.register(balloon_type, balloon_type_admin)

class balloon_sub_type_admin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name_cn", "name_en", "main_type", "order")


admin.site.register(balloon_sub_type, balloon_sub_type_admin)



class balloon_admin(SortableAdminMixin, admin.ModelAdmin):

    ordering = ["order","type"]
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    admin_thumbnail.template =  'admin_thumbnail.html'
    list_display = ("name_cn", "name_en","main_type", "type","admin_thumbnail","order")

    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }

    change_form_template = "balloon_sub_menu.html"




admin.site.register(balloon, balloon_admin)
