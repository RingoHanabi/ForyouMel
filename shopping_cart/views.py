from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def shopping_cart_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("shopping cart en")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("shopping cart cn")

    return render(request, 'shopping_cart_en.html',{'page_title':"Shopping Cart"})

def shopping_cart_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("shopping cart en")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("shopping cart cn")
    return render(request, 'shopping_cart_cn.html',{'page_title':"购物车"})


def checkout_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("checkout en")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("checkout cn")
    return HttpResponse("Checkout English")


def checkout_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("checkout en")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("checkout cn")

    return HttpResponse("Checkout Chinese")
