from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import party_decoration, party_decoration_type, party_decoration_sub_type
import json


# Create your views here.
def party_decoration_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_decoration")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_decoration cn")

    all_party_decorations = party_decoration.objects.all()
    all_party_decoration_types = party_decoration_type.objects.all()
    all_party_decoration_sub_types = party_decoration_sub_type.objects.all()
    return render(request, 'party_decorations.html',{'page_title':"Our party_decorations","types":all_party_decoration_types, "sub_types": all_party_decoration_sub_types,"party_decorations":all_party_decorations})

def party_decoration_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_decoration")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_decoration cn")
    all_party_decorations = party_decoration.objects.all()
    all_party_decoration_types = party_decoration_type.objects.all()
    all_party_decoration_sub_types = party_decoration_sub_type.objects.all()

    return render(request, 'party_decorations_cn.html',{'page_title':"气球装饰","types":all_party_decoration_types,"sub_types": all_party_decoration_sub_types,"party_decorations":all_party_decorations})

def party_decoration_details_en(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_decoration details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_decoration details cn", id = id)
    party_decoration_detail = party_decoration.objects.all().filter(id = id).first()
    return render(request, 'party_decoration_details.html',{'page_title':"party_decoration: "+party_decoration_detail.name_en,"party_decoration":party_decoration_detail})

def party_decoration_details_cn(request,id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_decoration details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_decoration details cn", id = id)
    party_decoration_detail = party_decoration.objects.all().filter(id = id).first()

    return render(request, 'party_decoration_details_cn.html',{'page_title':"气球装饰: "+party_decoration_detail.name_cn,"party_decoration":party_decoration_detail})

def party_decoration_type_en(request,type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_decoration type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_decoration type cn", type_id)

    all_party_decorations = party_decoration.objects.all()
    all_party_decoration_types = party_decoration_type.objects.all()
    all_party_decoration_sub_types = party_decoration_sub_type.objects.all()
    this_type = all_party_decoration_sub_types.filter(id=type_id).first()

    return render(request, 'party_decorations_type.html',
                  {'page_title': "Our party_decorations", "types": all_party_decoration_types, "sub_types": all_party_decoration_sub_types,
                   "party_decorations": all_party_decorations, "this_type": this_type})


def party_decoration_type_cn(request, type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_decoration type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_decoration type cn", type_id)

    all_party_decorations = party_decoration.objects.all()
    all_party_decoration_types = party_decoration_type.objects.all()
    all_party_decoration_sub_types = party_decoration_sub_type.objects.all()
    this_type = all_party_decoration_sub_types.filter(id=type_id).first()

    return render(request, 'party_decorations_type_cn.html',
                  {'page_title': "Our party_decorations", "types": all_party_decoration_types, "sub_types": all_party_decoration_sub_types,
                   "party_decorations": all_party_decorations, "this_type": this_type})

def post_party_decoration_maintypes(request):
    if request.is_ajax and request.method == "POST":
        main_types = party_decoration_type.objects.all()
        return_data = []
        for each in main_types:
            return_data.append([each.id, each.name_cn])
        return_data = json.dumps(return_data)
        return JsonResponse(return_data, status=200, safe=False)


def post_party_decoration_subtypes(request):
    if request.is_ajax and request.method == "POST":
        main_type_id = request.POST.get("main_type_id", None)
        sub_types = party_decoration_sub_type.objects.all().filter(main_type=main_type_id)
        return_data = []
        for each in sub_types:
            return_data.append([each.id, each.__str__()])

        return_data = json.dumps(return_data)
        return JsonResponse(return_data, status=200, safe=False)
