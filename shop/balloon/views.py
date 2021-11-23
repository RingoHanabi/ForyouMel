from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import balloon, balloon_type

# Create your views here.
def balloon_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon cn")

    all_balloons = balloon.objects.all()
    all_balloon_types = balloon_type.objects.all()
    page_data = []
    for types in all_balloon_types:
        temp = []
        for each in all_balloons:
            if each.type.name_cn == types.name_cn:
                temp.append(each)
        page_data.append(temp)
    print(page_data)
    return render(request, 'balloons.html',{'page_title':"Our Balloons","types":all_balloon_types,"balloons":all_balloons})

def balloon_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon cn")
    all_balloons = balloon.objects.all()
    all_balloon_types = balloon_type.objects.all()
    page_data = []
    for types in all_balloon_types:
        temp = []
        for each in all_balloons:
            if each.type.name_cn == types.name_cn:
                temp.append(each)
        page_data.append(temp)
    print(page_data)
    return render(request, 'balloons_cn.html',{'page_title':"气球装饰","types":all_balloon_types,"balloons":all_balloons})

def balloon_details_en(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon details cn", id = id)
    print(id)
    balloon_detail = balloon.objects.all().filter(id = id).first()
    return render(request, 'balloon_details.html',{'page_title':"Balloon: "+balloon_detail.name_en,"balloon":balloon_detail})

def balloon_details_cn(request,id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon details cn", id = id)
    balloon_detail = balloon.objects.all().filter(id = id).first()

    return render(request, 'balloon_details_cn.html',{'page_title':"气球装饰: "+balloon_detail.name_cn,"balloon":balloon_detail})
