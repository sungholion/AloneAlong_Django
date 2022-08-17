from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.contrib import auth
from .models import User
from communityapp.models import Blog

def login_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        #POST일땐 로그인 기능을 수행함
        user = auth.authenticate(request,
            username=request.POST["id"],
            password=request.POST["pw"]
        )
        posts=Blog.objects.filter().order_by('-date')
        if user != None:
            auth.login(request, user)
            return render(request, "index.html", {"user":user, "posts" : posts})
        else:
            return render(request, "login.html", {"isLoginFail": True, "posts" : posts})
def logout(request):
    auth.logout(request)
    return redirect("index")

def signup_signup(request):
    #회원가입도 엄연히 DB상에 저장되는거라서 터미널에 migrate해야하냐고 생각할 수 있지만, user클래스의 힘을 빌리면 필요없다.
    if request.method == "GET":
        return render(request, "signup.html")
    else:
        #POST일땐 회원가입 기능을 수행함
        #signup.html에서 사용자가 친 아이디와 비밀번호가 여기에 도착함
        #사용자가 친 아이디의 필드이름은 username
        #비밀번호는 pw, 확인비밀번호는 pw2이다.
        if request.POST["pw"] == request.POST["pw2"]:
            user_new = User.objects.create(username=request.POST["username"],
                nickname=request.POST["nickname"],
                introduction=request.POST["introduction"],
                mainCategory=request.POST["mainCategory"],
                profilePhoto=request.FILES.get("profilePhoto")
            )
            #아래 두줄을 보면 패스워드를 위에 create에서 안받고 따로 메소드를 사용하는 것을 볼 수 있다.
            #위에 create에서 패스워드를 받을때, 유저가 친 패스워드가 허접하면 로그인안되는 예외가 발생한다.
            #따라서 아래 두줄 방법으로 패스워드를 받았다. 단 이 방법의 단점은 .save()를 꼭해야한다는점.
            user_new.set_password(request.POST["pw"])
            user_new.save()
            return redirect("login")
        else:
            return render(request, "signup.html", {"isPasswordDiffer": True})
    

