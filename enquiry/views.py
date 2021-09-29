from django.shortcuts import render
from enquiry.forms import EnquiryForm
# Create your views here.
def enquiry(request):
    if request.method == 'POST':
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