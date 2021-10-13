from django.shortcuts import render, redirect
from enquiry.forms import EnquiryForm
# Create your views here.
def enquiry_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        print("English")
        return redirect("enquiry")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        print("Chinese")

        return redirect("enquiry_cn")
    if request.method == 'POST' and 'name' in request.POST:
        print(request.POST)
        form = EnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            print(name+email+phone+subject+body)
            form.save()
    form = EnquiryForm()
    return render(request, 'enquiry_cn.html',{'form':form,'page_title':"Contact Us"})

def enquiry(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        print("English")
        return redirect("enquiry")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        print("Chinese")

        return redirect("enquiry_cn")
    if request.method == 'POST' and 'name' in request.POST:
        print(request.POST)
        form = EnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            print(name+email+phone+subject+body)
            form.save()
    form = EnquiryForm()
    return render(request, 'enquiry.html',{'form':form,'page_title':"Contact Us"})