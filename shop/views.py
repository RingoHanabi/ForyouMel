from django.shortcuts import render, redirect
# Create your views here.
def flower(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower cn")
    return render(request, 'flowers.html',{'page_title':"Our Flowers"})

def balloon(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon cn")
    return render(request, 'balloon.html',{'page_title':"Our Balloons"})

def party(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party cn")
    return render(request, 'party_goods.html',{'page_title':"Our Party Hires"})

def wedding(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding cn")
    return render(request, 'wedding.html',{'page_title':"Our Wedding Decoration"})

def flower_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("flower")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("flower cn")
    return render(request, 'flowers_cn.html',{'page_title':"花卉 花束"})

def balloon_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("balloon")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("balloon cn")
    return render(request, 'balloon_cn.html',{'page_title':"气球装饰"})

def party_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("party")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("party cn")
    return render(request, 'party_goods_cn.html',{'page_title':"聚会用品租赁"})

def wedding_cn(request):
    if request.method == 'POST' and request.POST["language"] == "English":
        return redirect("wedding")
    if request.method == 'POST' and request.POST["language"] == "Chinese":
        return redirect("wedding cn")
    return render(request, 'wedding_cn.html',{'page_title':"婚礼装扮"})

