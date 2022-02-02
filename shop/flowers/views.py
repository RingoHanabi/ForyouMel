from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import flower, flower_type, flower_sub_type
import json


# Create your views here.
def flower_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower cn")

    all_flowers = flower.objects.all()
    all_flower_types = flower_type.objects.all()
    all_flower_sub_types = flower_sub_type.objects.all()
    return render(request, 'flowers.html',
                  {'page_title': "Our Flowers", "types": all_flower_types, "sub_types": all_flower_sub_types,
                   "flowers": all_flowers})


def flower_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower cn")
    all_flowers = flower.objects.all()
    all_flower_types = flower_type.objects.all()
    all_flower_sub_types = flower_sub_type.objects.all()
    return render(request, 'flowers_cn.html',
                  {'page_title': "花束 & 花卉", "types": all_flower_types, "sub_types": all_flower_sub_types,
                   "flowers": all_flowers})


def flower_type_en(request,type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower type cn", type_id)

    all_flowers = flower.objects.all()
    all_flower_types = flower_type.objects.all()
    all_flower_sub_types = flower_sub_type.objects.all()
    this_type = all_flower_sub_types.filter(id=type_id).first()

    return render(request, 'flowers_type.html',
                  {'page_title': "Our Flowers", "types": all_flower_types, "sub_types": all_flower_sub_types,
                   "flowers": all_flowers, "this_type": this_type})


def flower_type_cn(request, type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower type cn", type_id)

    all_flowers = flower.objects.all()
    all_flower_types = flower_type.objects.all()
    all_flower_sub_types = flower_sub_type.objects.all()
    this_type = all_flower_sub_types.filter(id=type_id).first()

    return render(request, 'flowers_type_cn.html',
                  {'page_title': "Our Flowers", "types": all_flower_types, "sub_types": all_flower_sub_types,
                   "flowers": all_flowers, "this_type": this_type})


def flower_details_en(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower details", id=id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower details cn", id=id)
    flower_detail = flower.objects.all().filter(id=id).first()
    all_flowers = flower.objects.all()
    all_flower_types = flower_type.objects.all()
    all_flower_sub_types = flower_sub_type.objects.all()

    return render(request, 'flowers_details.html',
                  {'page_title': "Our Flowers: " + flower_detail.name_en, "flower": flower_detail, "types": all_flower_types, "sub_types": all_flower_sub_types,
                   "flowers": all_flowers})


def flower_details_cn(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower details", id=id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower details cn", id=id)
    flower_detail = flower.objects.all().filter(id=id).first()

    return render(request, 'flowers_details_cn.html',
                  {'page_title': "花束:" + flower_detail.name_cn, "flower": flower_detail})


def post_flower_maintypes(request):
    if request.is_ajax and request.method == "POST":
        main_types = flower_type.objects.all()
        return_data = []
        for each in main_types:
            return_data.append([each.id, each.name_cn])
        return_data = json.dumps(return_data)
        return JsonResponse(return_data, status=200, safe=False)


def post_flower_subtypes(request):
    if request.is_ajax and request.method == "POST":
        main_type_id = request.POST.get("main_type_id", None)
        sub_types = flower_sub_type.objects.all().filter(main_type=main_type_id)
        return_data = []
        for each in sub_types:
            return_data.append([each.id, each.__str__()])

        return_data = json.dumps(return_data)
        return JsonResponse(return_data, status=200, safe=False)
