from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
import json

# Create your views here.
from shop.party_decoration.models import party_decoration
from shop.flowers.models import flower
from shop.party_hire.models import party_hire

from shop.models import Product


def shopping_cart_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("shopping cart en")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("shopping cart cn")

    print(request.COOKIES)
    cart = json.loads(request.COOKIES["cart"])

    products = Product.objects.all()

    data = []
    total = 0
    for item in cart:
        product = products.filter(id=item).first()
        product_type = {}
        if (len(flower.objects.all().filter(id=product.id)) != 0):
            product = flower.objects.all().filter(id=product.id).first()
            product_type = {
                "en": "Flowers",
                "cn": "花卉"
            }
        elif (len(party_decoration.objects.all().filter(id=product.id)) != 0):
            product = party_decoration.objects.all().filter(id=product.id).first()
            product_type = {
                "en": "party_decoration",
                "cn": "气球"
            }

        elif (len(party_hire.objects.all().filter(id=product.id)) != 0):
            product = party_hire.objects.all().filter(id=product.id).first()
            product_type = {
                "en": "Party Hire",
                "cn": "聚会用品"
            }

        quantity = cart[item]['quantity']
        subtotal = int(quantity) * product.price
        total += subtotal
        data.append([product, quantity, subtotal, product_type])

    print(data)
    return render(request, 'shopping_cart_en.html', {'page_title': "Shopping Cart", "data": data, "total": total})


def shopping_cart_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("shopping cart en")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("shopping cart cn")

    print(request.COOKIES)
    cart = json.loads(request.COOKIES["cart"])

    products = Product.objects.all()

    data = []
    total = 0
    for item in cart:
        product = products.filter(id=item).first()
        product_type = {}
        if (len(flower.objects.all().filter(id=product.id)) != 0):
            product = flower.objects.all().filter(id=product.id).first()
            product_type = {
                "en": "Flowers",
                "cn": "花卉"
            }
        elif (len(party_decoration.objects.all().filter(id=product.id)) != 0):
            product = party_decoration.objects.all().filter(id=product.id).first()
            product_type = {
                "en": "party_decoration",
                "cn": "气球"
            }

        elif (len(party_hire.objects.all().filter(id=product.id)) != 0):
            product = party_hire.objects.all().filter(id=product.id).first()
            product_type = {
                "en": "Party Hire",
                "cn": "聚会用品"
            }

        quantity = cart[item]['quantity']
        subtotal = int(quantity) * product.price
        total += subtotal
        data.append([product, quantity, subtotal, product_type])

    print(data)
    return render(request, 'shopping_cart_cn.html', {'page_title': "Shopping Cart", "data": data, "total": total})


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
