from django.contrib import admin
from django.contrib.admin import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.html import format_html
from imagekit.admin import AdminThumbnail
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import flower, flower_type, flower_sub_type


class AdminImageWidget(AdminFileWidget):
    """Admin widget for showing clickable thumbnail of Image file fields"""

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and getattr(value, 'url', None):
            html = format_html(
                '<a href="{0}" target="_blank"><img src="{0}" alt="{1}" width="150" height="150" style="object-fit: contain;"/></a>',
                value.url, str(value)) + html
        return html


# Register your models here.


class flower_type_admin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name_cn","order" ,"name_en")

admin.site.register(flower_type, flower_type_admin)


class flower_sub_type_admin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name_cn", "order", "name_en", "main_type")

admin.site.register(flower_sub_type, flower_sub_type_admin)


class flower_admin(SortableAdminMixin, admin.ModelAdmin):



    ordering = ["order", "type"]
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    admin_thumbnail.template = 'admin_thumbnail.html'
    list_display = ("name_cn", "order", "name_en", "main_type","type", "admin_thumbnail")

    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }

    change_form_template = "flower_sub_menu.html"


admin.site.register(flower, flower_admin)
