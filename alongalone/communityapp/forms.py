from django import forms
from .models import Blog,Comment

#django modelform (html form / django form은 사용 x)
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog  #어떤 모델을 기반으로 자동으로 form을 생성할 것인지
        #fields = '__all__' #모든 필드 입력받음
        fields = ['title','body', 'photo'] #특정 필드만 입력받음

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        # fields = ['title', 'body']
