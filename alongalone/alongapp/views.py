from django.shortcuts import redirect, render
from communityapp.views import honbabdetail
"""뷰의 이름 규칙
그냥 렌더를 위한 단순 뷰면은 해당 html의 이름으로 정함
렌더말고도 다른 기능이 있으면 "기능_html이름"으로 짓는다.
"""
def index(request):
    return render(request, "index.html")

def map(request):
    pass

def sponsor_status(request):
    if request.user.is_authenticated:
        return render(request, "sponsor_status.html")
    else:
        return redirect("login")

def sponsor(request):
    if request.user.is_authenticated:
        return render(request, "sponsor.html")
    else:
        return redirect("login")

def charge(request, money):
    user = request.user
    user.cash += money
    user.save()
    return render(request, "sponsor.html")

def donate(request, blog_id):
    money_donate = int(request.POST["money"])
    if request.user.cash < money_donate:
        #돈부족
        return render(request, "sponsor.html")
    else:
        #돈충분
        user = request.user
        user.cash -= money_donate
        user.save()
        return honbabdetail(request, blog_id)


########프론트엔드 파일을 가져온거 디버깅용 임시 뷰
def base(request):
    return render(request, "base.html")

def detailpost(request):
    return render(request, "detailpost_백엔드기다리는 중.html")

def map_popup(request):
    return render(request, "map_popup.html")

def myprofile_fin(request):
    return render(request, "myprofile_fin.html")

def saessakcount(request):
    return render(request, "saessakcount_백엔드 기다리는 중.html")

def honmap(request):
    return render(request, "honmap.html")

def honmap2(request):
    return render(request, "honmap2.html")

"""
def sponsor_status(request):
    return render(request, "sponsor_status.html")

def sponsor(request):
    return render(request, "sponsor.html")
"""
def write_back(request):
    return render(request, "write_back.html")