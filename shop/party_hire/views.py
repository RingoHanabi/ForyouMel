from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import party_hire, party_hire_type

# Create your views here.
def party_hire_en(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_hire")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_hire cn")

    all_party_hires = party_hire.objects.all()
    all_party_hire_types = party_hire_type.objects.all()
    page_data = []
    for types in all_party_hire_types:
        temp = []
        for each in all_party_hires:
            if each.type.name_cn == types.name_cn:
                temp.append(each)
        page_data.append(temp)
    print(page_data)
    return render(request, 'party_hire.html',{'page_title':"Our Party Hire","types":all_party_hire_types,"party_hires":all_party_hires})

def party_hire_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party_hire")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party_hire cn")
    all_party_hires = party_hire.objects.all()
    all_party_hire_types = party_hire_type.objects.all()
    page_data = []
    for types in all_party_hire_types:
        temp = []
        for each in all_party_hires:
            if each.type.name_cn == types.name_cn:
                temp.append(each)
        page_data.append(temp)
    print(page_data)
    return render(request, 'party_hire_cn.html',{'page_title':"聚会装饰用品","types":all_party_hire_types,"party_hires":all_party_hires})

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
