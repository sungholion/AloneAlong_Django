# models.py 해커톤 당일 기준 변동 사항 - heart 필드추가 (프론트 영향 x)
# comment의 comment_user 필드 추가 - 댓글 입력자 닉네임 표시(상의 필요) + honbabdetail.html도 봐야함.
from django.db import models
from accountapp.models import User

class Blog(models.Model):
    CATEGORY_CHOICES = (
		('1', '혼밥'),
        ('2', '혼술'),
        ('3', '혼카페'),
        ('4', '혼놀')
    ) 
    
    id = models.BigAutoField(help_text="Post ID", primary_key=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=3, choices = CATEGORY_CHOICES, default = "1") 
    photo = models.ImageField(blank=True, null =True, upload_to ='blog_photo')  
    body = models.TextField()
    location = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)  #현재 시간을 자동으로 추가.
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE, db_column="author", blank=False)
    heart = models.PositiveIntegerField(default=0)
    #category = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_question')
    #첫번째 인자가 연결할 객체 / CASCADE가 객체가 사라질 경우 같이 사라진다는 뜻.

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.comment
