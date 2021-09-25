from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from .models import Enquiry


# class EnquiryForm(forms.Form):
#     name = forms.CharField()
#     phone = forms.CharField(label = "Phone")
#     email = forms.EmailField(label = "E-Mail")
#     subject = forms.CharField()
#     body = forms.CharField(widget=forms.Textarea)

class EnquiryForm(forms.ModelForm):

     class Meta:
        model = Enquiry
        fields = ('name','phone','email','subject','body')

     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.helper = FormHelper
         self.helper.form_method = 'post'
         self.helper.layout = Layout(
             Field('name', css_class="form-group form-control"),
             Field('phone', css_class="form-group form-control"),
             Field('email', css_class="form-group form-control"),
             Field('subject', css_class="form-group form-control"),
             Field('body', css_class="form-group form-control"),
             Submit('submit','Submit', css_class='btn-success')
         )