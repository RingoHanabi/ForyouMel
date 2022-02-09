from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import party_hire, party_hire_type, party_hire_sub_type
import json


# Create your views here.
def party_hire_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_hire")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_hire cn")

    all_party_hires = party_hire.objects.all()
    all_party_hire_types = party_hire_type.objects.all()
    all_party_hire_sub_types = party_hire_sub_type.objects.all()

    return render(request, 'party_hire.html',{'page_title':"Our Party Hire","sub_types":all_party_hire_sub_types,"types":all_party_hire_types,"party_hires":all_party_hires})

def party_hire_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_hire")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_hire cn")
    all_party_hires = party_hire.objects.all()
    all_party_hire_types = party_hire_type.objects.all()
    all_party_hire_sub_types = party_hire_sub_type.objects.all()

    return render(request, 'party_hire_cn.html',{'page_title':"聚会装饰用品","sub_types":all_party_hire_sub_types,"types":all_party_hire_types,"party_hires":all_party_hires})

def party_hire_details_en(request, id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_hire details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_hire details cn", id = id)
    print(id)
    party_hire_detail = party_hire.objects.all().filter(id = id).first()
    return render(request, 'party_hire_details.html',{'page_title':"Party Hire: "+party_hire_detail.name_en,"party_hire":party_hire_detail})

def party_hire_details_cn(request,id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_hire details", id = id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_hire details cn", id = id)
    party_hire_detail = party_hire.objects.all().filter(id = id).first()

    return render(request, 'party_hire_details_cn.html',{'page_title':"聚会装饰: "+party_hire_detail.name_cn,"party_hire":party_hire_detail})

def party_hire_type_en(request,type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_hire type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_hire type cn", type_id)

    all_party_hires = party_hire.objects.all()
    all_party_hire_types = party_hire_type.objects.all()
    all_party_hire_sub_types = party_hire_sub_type.objects.all()
    this_type = all_party_hire_sub_types.filter(id=type_id).first()

    return render(request, 'party_hires_type.html',
                  {'page_title': "Our party_hires", "types": all_party_hire_types, "sub_types": all_party_hire_sub_types,
                   "party_hires": all_party_hires, "this_type": this_type})


def party_hire_type_cn(request, type_id):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_hire type", type_id)
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_hire type cn", type_id)

    all_party_hires = party_hire.objects.all()
    all_party_hire_types = party_hire_type.objects.all()
    all_party_hire_sub_types = party_hire_sub_type.objects.all()
    this_type = all_party_hire_sub_types.filter(id=type_id).first()

    return render(request, 'party_hires_type_cn.html',
                  {'page_title': "Our party_hires", "types": all_party_hire_types, "sub_types": all_party_hire_sub_types,
                   "party_hires": all_party_hires, "this_type": this_type})

def post_party_hire_maintypes(request):
    if request.is_ajax and request.method == "POST":
        main_types = party_hire_type.objects.all()
        return_data = []
        for each in main_types:
            return_data.append([each.id, each.name_cn])
        return_data = json.dumps(return_data)
        return JsonResponse(return_data, status=200, safe=False)


def post_party_hire_subtypes(request):
    if request.is_ajax and request.method == "POST":
        main_type_id = request.POST.get("main_type_id", None)
        sub_types = party_hire_sub_type.objects.all().filter(main_type=main_type_id)
        return_data = []
        for each in sub_types:
            return_data.append([each.id, each.__str__()])

        return_data = json.dumps(return_data)
        return JsonResponse(return_data, status=200, safe=False)
