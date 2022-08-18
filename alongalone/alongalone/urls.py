"""alongalone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from alongapp import views
from accountapp import views as accountapp_views
from communityapp import views as communityapp_views
from commentapp import views as commentapp_views
"""
주의사항:
    각 앱마다 views이름이 똑같으니 윗줄에 as ~로 views를 앱마다 구분했으니
    path 두번째 인자 적을때 헷갈리지말것.
"""
urlpatterns = [
    path('admin/', admin.site.urls),

    #alongapp 관련 URL
    #path("", views.index, name="index"),
    path("map/", views.map, name="map"),
        #alongapp에서 후원관련 URL
    path("donate_detailpost/<int:blog_id>", views.donate, name="donate"),
    path("sponsor_status/", views.sponsor_status, name="sponsor_status"),
    path("sponsor/", views.sponsor, name="sponsor"),
    path("charge/<int:money>", views.charge, name="charge"),
    path("donate/<int:blog_id>", views.donate, name="donate"),

    #accountapp 관련 URL
    path("login/", accountapp_views.login_login, name="login"),
    path("logout/", accountapp_views.logout, name="logout"),
    path("signup/", accountapp_views.signup_signup, name="signup"),

    ##########################  communityapp 관련 URL  ################################################
    path("", communityapp_views.index, name="index"), 
    path('create/', communityapp_views.create, name='create'),
    path("honbabwrite/", communityapp_views.honbabwrite, name="honbabwrite"),

    
    ## 각 게시글들의 상세 페이지 url
    path('honbabdetail/<int:blog_id>', communityapp_views.honbabdetail, name = 'honbabdetail'),
    path('honbabdetail/<int:blog_id>/delete', communityapp_views.honbabdetail_delete, name = 'honbabdetail_delete'),
    path('honbabdetail/<int:blog_id>/update', communityapp_views.honbabdetail_update, name = 'honbabdetail_update'),
     ##아래 한줄 인희작성
    path("honbabdetail/<int:blog_id>/map/", communityapp_views.honbabdetail_map, name="honbabdetail_map"),
    path("myprofile_fin/", communityapp_views.myprofile_fin, name="myprofile_fin"),
    path('create_comment/<int:blog_id>', communityapp_views.create_comment , name="create_comment"),





    #############프론트에서 가져온거 확인용 임시 URL
    path("base/", views.base, name="base"),
    path("detailpost/", views.detailpost, name="detailpost"),
    path("map_popup/", views.map_popup, name="map_popup"),
    path("saessakcount/", views.saessakcount, name="saessakcount"),
    path("sponsor_status/", views.sponsor_status, name="sponsor_status"),
    #path("sponsor/", views.sponsor, name="sponsor"),
    path("write_back/", views.write_back, name="writes_back"),
    path("honmap/", views.honmap, name="honmap"),
    path("honmap2/", views.honmap2, name="honmap2"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
