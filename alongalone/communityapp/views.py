from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogModelForm, CommentForm
from accountapp.models import User

def index(request):
    posts =Blog.objects.filter().order_by('-date')   #필터링해서 가져오기 날짜 오름차순(date) 내림차순(-date)
    return render(request, 'index.html', {'posts' : posts}) 

##  1. html을 이용한 form 작성 - 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST' or request.method =='FILES'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.category = request.POST['category']
        post.photo = request.FILES.get('photo')    #사진이 있으면 저장하고, 없으면 none
        post.location = request.POST['location']
        post.author = request.user
        post.date = timezone.now()
        post.save()
    return redirect('index')

# 2. django form을 이용해서 입력값을 받는 함수
# GET 요청과 (= 입력값을 받을 수 있는 html을 갖다 줘야함)
# POST 요청 (= 입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리)
# 둘 다 처리가 가능한 함수 
def honbabcreate(request):
    if(request.method == 'POST' or request.method =='FILES'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.category = request.POST['category']
        post.photo = request.FILES['photo']
        post.date = timezone.now()
        post.save()
    return redirect('index')

## 3.django modelform을 이용해서 입력값을 받는 함수(새 글 생성하기 눌렀을 때 함수)
def honbabwrite(request):

    context = dict()    
    # render함수의 3번째 인자로 views에서 html로 데이터를 넘길 때, 데이터 종류가 많아질 수 있어서 context에 묶는 역할

    #새 글 생성하기를 누르면 데이터베이스로 넘기기
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            temp_form = form.save(commit = False)   #당장 저장하지 말고 잠시 멈추고, temp form에 담음
            temp_form.category = "혼밥 게시판"  #사용자 선택을 어떻게 반영하지(아직 미구현)
            form.save()
            return redirect('index')

    #새 글을 입력받는 form을 띄워주기
    else:
        context['form'] = BlogModelForm()
    return render(request, 'honbabwrite.html', context) 

def honbabdetail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id) #특정 pk값을 가지는 객체 하나만 가져오기
    comment_form = CommentForm()
    user_author = get_object_or_404(User, pk = blog_detail.author)
    current_posts = Blog.objects.filter(author = user_author.username).order_by('-date')[:3]
    #posts = Blog.objects.all() #블로그 객체를 모두 가져오는 코드
    #posts =Blog.objects.filter().order_by('-date')   #객체 필터링해서 가져오기 날짜 오름차순(date) 내림차순(-date)
    return render(request, 'honbabdetail.html', {'blog_detail' : blog_detail, 'user_author' : user_author, 'current_posts' : current_posts, 'comment_form':comment_form} )

def honbabdetail_delete(request, blog_id):
    post = Blog.objects.get(pk = blog_id)
    post.delete()
    return redirect('index')

def honbabdetail_update(request, blog_id):
  post = Blog.objects.get(id=blog_id)
  if request.method == "POST" or request.method == "FILES":
    post.title = request.POST['title']
    post.body = request.POST['body']
    post.date = timezone.now()
    try:
      post.image = request.FILES['photo']
    except:
      post.image = None
    post.save()
    return redirect('index')
  else:
    post=Blog()
    return render(request, 'update.html', {'post':post})
##인희작성 : 세부페이지에서 세부맵으로 이동하는 함수
def honbabdetail_map(request, blog_id):
    location_detailpost = Blog.objects.get(pk=blog_id).location
    detailposts_location = Blog.objects.filter(location=location_detailpost).exclude(pk=blog_id)[:3]
    num_detailposts_location = len(Blog.objects.filter(location=location_detailpost))
    return render(request, "map_popup.html", {"location" : location_detailpost, "otherPosts":detailposts_location, "numPosts":num_detailposts_location})

##댓글
def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST) #post 요청으로 넘어온 form data들을 CommentForm양식에 담아서 filled_form으로 저장
    if filled_form.is_valid():    
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()
    return redirect('honbabdetail', blog_id) #redirect('애칭', parameter) 해주면 google.com/1 이런식으로 뒤에 붙는 값을 지정해줄수있다.

#프로필 함수
def myprofile_fin(request):
    posts = Blog.objects.filter(author=request.user.username).order_by('-date')[0:3]
    posts2 = Blog.objects.filter(author=request.user.username).order_by('-date')[3:6]
    #current_user=request.user
    #posts_6 = Blog.objects.filter(author=current_user)[:6]
    return render(request, 'myprofile_fin.html', {'posts' : posts, 'posts2' : posts2})