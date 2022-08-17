from django.db import models
from accountapp.models import User

# class 새로 만들거나 변경할 때마다 데이터베이스에 반영해줘야 함. ( makemigrations -> migrate 잊지 말기)
# 장고는 우리가 primary key 지정안하면 id라는 키를 자동으로 만듬.

class Blog(models.Model):
    CATEGORY_CHOICES = (
		('1', '혼밥'),
        ('2', '혼술'),
        ('3', '혼카페'),
        ('4', '혼놀')

    ) #글작성 화면에서 어떤 게시판에 쓸 지 카테고리를 정하면 혼밥은 1, 혼술은 2 이런 식으로 value 저장됌.
    
    id = models.BigAutoField(help_text="Post ID", primary_key=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=3, choices = CATEGORY_CHOICES, default = "1") #어떤 게시판에 글을 쓸 것인지 카테고리 선택
    photo = models.ImageField(blank=True, null =True, upload_to ='blog_photo')   #자동으로 media 파일 하에 blog_photo 폴더 생성 및 파일 저장
    body = models.TextField()
    location = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)  #현재 시간을 자동으로 추가.
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE, db_column="author", blank=False)
    

    #category = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_question')
    #첫번째 인자가 연결할 객체 / CASCADE가 객체가 사라질 경우 같이 사라진다는 뜻.

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
