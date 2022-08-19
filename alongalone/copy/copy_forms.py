# 해커톤 당일 기준 forms.py 변경 사항 - CommentForm삭제
# 대신 honbabdetail.html에서 받아옴. (상의 후 변경)
from django import forms
from .models import Blog,Comment

#django modelform (html form / django form은 사용 x)
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog  #어떤 모델을 기반으로 자동으로 form을 생성할 것인지
        #fields = '__all__' #모든 필드 입력받음
        fields = ['title','body', 'photo'] #특정 필드만 입력받음
 
""" 여기가 변경사항. 이제 CommentForm안씀.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        # fields = ['title', 'body']
"""