from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'contact.html', {'page_title':"Contact Us"})