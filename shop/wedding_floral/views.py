from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import wedding_floral, wedding_floral_type

# Create your views here.
def wedding_floral_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding_floral")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding_floral cn")

    all_wedding_florals = wedding_floral.objects.all()
    all_wedding_floral_types = wedding_floral_type.objects.all()
    page_data = []
    for types in all_wedding_floral_types:
        temp = []
        for each in all_wedding_florals:
            if each.type.name_cn == types.name_cn:
                temp.append(each)
        page_data.append(temp)
    print(page_data)
    return render(request, 'wedding_floral.html', {'page_title': "Our wedding_floral Scene", "types":all_wedding_floral_types, "wedding_florals":all_wedding_florals})

def wedding_floral_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding_floral")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding_floral cn")
    all_wedding_florals = wedding_floral.objects.all()
    all_wedding_floral_types = wedding_floral_type.objects.all()
    page_data = []
    for types in all_wedding_floral_types:
        temp = []
        for each in all_wedding_florals:
            if each.type.name_cn == types.name_cn:
                temp.append(each)
        page_data.append(temp)
    print(page_data)
    return render(request, 'wedding_floral_cn.html', {'page_title': "婚礼现场布置", "types":all_wedding_floral_types, "wedding_florals":all_wedding_florals})

def wedding_floral_details_en(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding_floral details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding_floral details cn", id = id)
    print(id)
    wedding_floral_detail = wedding_floral.objects.all().filter(id = id).first()
    return render(request, 'wedding_floral_details.html', {'page_title': "wedding_floral Scene: " + wedding_floral_detail.name_en, "wedding_floral":wedding_floral_detail})

def wedding_floral_details_cn(request,id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding_floral details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding_floral details cn", id = id)
    wedding_floral_detail = wedding_floral.objects.all().filter(id = id).first()

    return render(request, 'wedding_floral_details_cn.html', {'page_title': "婚礼现场: " + wedding_floral_detail.name_cn, "wedding_floral":wedding_floral_detail})


def wedding_floral_type_en(request,type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding_floral type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding_floral type cn", type_id)

    all_wedding_florals = wedding_floral.objects.all()
    all_wedding_floral_types = wedding_floral_type.objects.all()
    this_type = all_wedding_floral_types.filter(id=type_id).first()

    return render(request, 'wedding_floral_type.html',
                  {'page_title': "Our wedding_florals", "types": all_wedding_floral_types,
                   "wedding_florals": all_wedding_florals, "this_type": this_type})


def wedding_floral_type_cn(request, type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding_floral type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding_floral type cn", type_id)

    all_wedding_florals = wedding_floral.objects.all()
    all_wedding_floral_types = wedding_floral_type.objects.all()
    this_type = all_wedding_floral_types.filter(id=type_id).first()

    return render(request, 'wedding_floral_type_cn.html',
                  {'page_title': "Our wedding_florals", "types": all_wedding_floral_types,
                   "wedding_florals": all_wedding_florals, "this_type": this_type})
