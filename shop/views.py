from django.shortcuts import render
# Create your views here.
def flower(request):
    return render(request, 'flowers.html',{'page_title':"Our Flowers"})

def balloon(request):
    return render(request, 'balloon.html',{'page_title':"Our Balloons"})

def party(request):
    return render(request, 'party_goods.html',{'page_title':"Our Party Goods"})

def wedding(request):
    return render(request, 'wedding.html',{'page_title':"Our Wedding Decoration"})

