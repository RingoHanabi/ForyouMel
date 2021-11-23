from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import flower, flower_type

# Create your views here.
def flower_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower cn")

    all_flowers = flower.objects.all()
    all_flower_types = flower_type.objects.all()
    page_data = []
    for types in all_flower_types:
        temp = []
        for each in all_flowers:
            if each.type.name_cn == types.name_cn:
                temp.append(each)
        page_data.append(temp)
    print(page_data)
    return render(request, 'flowers.html',{'page_title':"Our Flowers","types":all_flower_types,"flowers":all_flowers})

def flower_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower cn")
    all_flowers = flower.objects.all()
    all_flower_types = flower_type.objects.all()
    page_data = []
    for types in all_flower_types:
        temp = []
        for each in all_flowers:
            if each.type.name_cn == types.name_cn:
                temp.append(each)
        page_data.append(temp)
    print(page_data)
    return render(request, 'flowers_cn.html',{'page_title':"花束&花卉","types":all_flower_types,"flowers":all_flowers})

def flower_details_en(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower details cn", id = id)
    print(id)
    flower_detail = flower.objects.all().filter(id = id).first()
    return render(request, 'flowers_details.html',{'page_title':"Our Flowers: "+flower_detail.name_en,"flower":flower_detail})

def flower_details_cn(request,id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower details cn", id = id)
    flower_detail = flower.objects.all().filter(id = id).first()

    return render(request, 'flowers_details_cn.html',{'page_title':"花束:"+flower_detail.name_cn,"flower":flower_detail})
