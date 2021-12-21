from django.shortcuts import render, redirect
from enquiry.forms import EnquiryForm
from django.contrib import messages
# Create your views here.
def enquiry_cn(request):
    if request.method == 'POST' and 'name' in request.POST:
        form = EnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            form.save()
        messages.add_message(request, messages.SUCCESS, "表单已成功上传，我们会尽快与您联系")
    elif request.method == 'POST' and request.POST["language"] == "English":
        return redirect("enquiry")
    elif request.method == 'POST' and request.POST["language"] == "Chinese":

        return redirect("enquiry_cn")

    form = EnquiryForm()
    return render(request, 'enquiry_cn.html',{'form':form,'page_title':"Contact Us"})

def enquiry(request):
    if request.method == 'POST' and 'name' in request.POST:
        form = EnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            form.save()
        messages.add_message(request, messages.SUCCESS, "The enquiry form is successfully submitted, we will get back to you so as we can")
    elif request.method == 'POST' and request.POST["language"] == "English":
        return redirect("enquiry")
    elif request.method == 'POST' and request.POST["language"] == "Chinese":

        return redirect("enquiry_cn")

    form = EnquiryForm()
    return render(request, 'enquiry.html',{'form':form,'page_title':"Contact Us"})