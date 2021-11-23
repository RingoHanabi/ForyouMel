from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import wedding, wedding_type

# Create your views here.
def wedding_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding cn")

    all_weddings = wedding.objects.all()
    all_wedding_types = wedding_type.objects.all()
    page_data = []
    for types in all_wedding_types:
        temp = []
        for each in all_weddings:
            if each.type.name_cn == types.name_cn:
                temp.append(each)
        page_data.append(temp)
    print(page_data)
    return render(request, 'wedding.html',{'page_title':"Our Wedding Scene","types":all_wedding_types,"weddings":all_weddings})

def wedding_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding cn")
    all_weddings = wedding.objects.all()
    all_wedding_types = wedding_type.objects.all()
    page_data = []
    for types in all_wedding_types:
        temp = []
        for each in all_weddings:
            if each.type.name_cn == types.name_cn:
                temp.append(each)
        page_data.append(temp)
    print(page_data)
    return render(request, 'wedding_cn.html',{'page_title':"婚礼现场布置","types":all_wedding_types,"weddings":all_weddings})

def wedding_details_en(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding details cn", id = id)
    print(id)
    wedding_detail = wedding.objects.all().filter(id = id).first()
    return render(request, 'wedding_details.html',{'page_title':"Wedding Scene: "+wedding_detail.name_en,"wedding":wedding_detail})

def wedding_details_cn(request,id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding details cn", id = id)
    wedding_detail = wedding.objects.all().filter(id = id).first()

    return render(request, 'wedding_details_cn.html',{'page_title':"婚礼现场: "+wedding_detail.name_cn,"wedding":wedding_detail})
