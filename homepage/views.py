from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return redirect("/home_cn")

def homepage_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        print("English")
        return redirect("homepage")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        print("Chinese")

        return redirect("homepage_cn")
    return render(request, 'homepage.html', {'page_title':"For you Flourist"})

def homepage_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("homepage")
    if request.method == 'POST' and request.POST["language"] == "Chinese":

        return redirect("homepage_cn")
    return render(request, 'homepage_cn.html', {'page_title':"For you Flourist"})