from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import balloon, balloon_type, balloon_sub_type
import json


# Create your views here.
def balloon_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon cn")

    all_balloons = balloon.objects.all()
    all_balloon_types = balloon_type.objects.all()
    all_balloon_sub_types = balloon_sub_type.objects.all()
    return render(request, 'balloons.html',{'page_title':"Our Balloons","types":all_balloon_types, "sub_types": all_balloon_sub_types,"balloons":all_balloons})

def balloon_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon cn")
    all_balloons = balloon.objects.all()
    all_balloon_types = balloon_type.objects.all()
    all_balloon_sub_types = balloon_sub_type.objects.all()

    return render(request, 'balloons_cn.html',{'page_title':"气球装饰","types":all_balloon_types,"sub_types": all_balloon_sub_types,"balloons":all_balloons})

def balloon_details_en(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon details cn", id = id)
    balloon_detail = balloon.objects.all().filter(id = id).first()
    return render(request, 'balloon_details.html',{'page_title':"Balloon: "+balloon_detail.name_en,"balloon":balloon_detail})

def balloon_details_cn(request,id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon details cn", id = id)
    balloon_detail = balloon.objects.all().filter(id = id).first()

    return render(request, 'balloon_details_cn.html',{'page_title':"气球装饰: "+balloon_detail.name_cn,"balloon":balloon_detail})

def balloon_type_en(request,type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon type cn", type_id)

    all_balloons = balloon.objects.all()
    all_balloon_types = balloon_type.objects.all()
    all_balloon_sub_types = balloon_sub_type.objects.all()
    this_type = all_balloon_sub_types.filter(id=type_id).first()

    return render(request, 'balloons_type.html',
                  {'page_title': "Our balloons", "types": all_balloon_types, "sub_types": all_balloon_sub_types,
                   "balloons": all_balloons, "this_type": this_type})


def balloon_type_cn(request, type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon type cn", type_id)

    all_balloons = balloon.objects.all()
    all_balloon_types = balloon_type.objects.all()
    all_balloon_sub_types = balloon_sub_type.objects.all()
    this_type = all_balloon_sub_types.filter(id=type_id).first()

    return render(request, 'balloons_type_cn.html',
                  {'page_title': "Our balloons", "types": all_balloon_types, "sub_types": all_balloon_sub_types,
                   "balloons": all_balloons, "this_type": this_type})

def post_balloon_maintypes(request):
    if request.is_ajax and request.method == "POST":
        main_types = balloon_type.objects.all()
        return_data = []
        for each in main_types:
            return_data.append([each.id, each.name_cn])
        return_data = json.dumps(return_data)
        return JsonResponse(return_data, status=200, safe=False)


def post_balloon_subtypes(request):
    if request.is_ajax and request.method == "POST":
        main_type_id = request.POST.get("main_type_id", None)
        sub_types = balloon_sub_type.objects.all().filter(main_type=main_type_id)
        return_data = []
        for each in sub_types:
            return_data.append([each.id, each.__str__()])

        return_data = json.dumps(return_data)
        return JsonResponse(return_data, status=200, safe=False)
