from django.contrib import admin

# Register your models here.
from django.shortcuts import redirect

from enquiry.models import Enquiry

class enquiry_admin(admin.ModelAdmin):
    list_display = ("subject","time","solved")
    list_filter = ("time",)
    change_form_template = "reply_button.html"

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context["email"] = enquiry_admin.get_object(self, request, object_id).email
        extra_context["time"] = enquiry_admin.get_object(self, request, object_id).time
        extra_context["name"] = enquiry_admin.get_object(self, request, object_id).name
        extra_context["body"] = enquiry_admin.get_object(self, request, object_id).body
        extra_context["subject"] = enquiry_admin.get_object(self, request, object_id).subject
        return super(enquiry_admin, self).changeform_view(request, object_id, form_url, extra_context = extra_context)


    def response_change(self, request, obj):
        if "_reply" in request.POST:
            email = obj.email
            redirect('mailto:'+email)
        return super().response_change(request, obj)


admin.site.site_header = 'Admin Site'
admin.site.register(Enquiry, enquiry_admin)
