from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import decoration, decoration_type, decoration_sub_type
import json


# Create your views here.
def decoration_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("decoration")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("decoration cn")

    all_decorations = decoration.objects.all()
    all_decoration_types = decoration_type.objects.all()
    all_decoration_sub_types = decoration_sub_type.objects.all()
    return render(request, 'decorations.html',
                  {'page_title': "Our decorations", "types": all_decoration_types, "sub_types": all_decoration_sub_types,
                   "decorations": all_decorations})


def decoration_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("decoration")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("decoration cn")
    all_decorations = decoration.objects.all()
    all_decoration_types = decoration_type.objects.all()
    all_decoration_sub_types = decoration_sub_type.objects.all()
    return render(request, 'decorations_cn.html',
                  {'page_title': "房间装饰", "types": all_decoration_types, "sub_types": all_decoration_sub_types,
                   "decorations": all_decorations})


def decoration_type_en(request, type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("decoration type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("decoration type cn", type_id)

    all_decorations = decoration.objects.all()
    all_decoration_types = decoration_type.objects.all()
    this_type = all_decoration_types.filter(id=type_id).first()
    all_decoration_sub_types = decoration_sub_type.objects.all()
    return render(request, 'decorations_type.html',
                  {'page_title': "Our decorations", "types": all_decoration_types, "sub_types": all_decoration_sub_types,
                   "decorations": all_decorations, "this_type": this_type})


def decoration_type_cn(request, type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("decoration type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("decoration type cn", type_id)

    all_decorations = decoration.objects.all()
    all_decoration_types = decoration_type.objects.all()
    this_type = all_decoration_types.filter(id=type_id)

    all_decoration_sub_types = decoration_sub_type.objects.all()
    return render(request, 'decorations_type_cn.html',
                  {'page_title': "Our decorations", "types": all_decoration_types, "sub_types": all_decoration_sub_types,
                   "decorations": all_decorations, "this_type": this_type})


def decoration_details_en(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("decoration details", id=id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("decoration details cn", id=id)
    decoration_detail = decoration.objects.all().filter(id=id).first()
    return render(request, 'decorations_details.html',
                  {'page_title': "Our decorations: " + decoration_detail.name_en, "decoration": decoration_detail})


def decoration_details_cn(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("decoration details", id=id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("decoration details cn", id=id)
    decoration_detail = decoration.objects.all().filter(id=id).first()

    return render(request, 'decorations_details_cn.html',
                  {'page_title': "花束:" + decoration_detail.name_cn, "decoration": decoration_detail})


def post_decoration_maintypes(request):
    if request.is_ajax and request.method == "POST":
        main_types = decoration_type.objects.all()
        return_data = []
        for each in main_types:
            return_data.append([each.id, each.name_cn])
        return_data = json.dumps(return_data)
        return JsonResponse(return_data, status=200, safe=False)


def post_decoration_subtypes(request):
    if request.is_ajax and request.method == "POST":
        main_type_id = request.POST.get("main_type_id", None)
        sub_types = decoration_sub_type.objects.all().filter(main_type=main_type_id)
        return_data = []
        for each in sub_types:
            return_data.append([each.id, each.__str__()])

        return_data = json.dumps(return_data)
        return JsonResponse(return_data, status=200, safe=False)
