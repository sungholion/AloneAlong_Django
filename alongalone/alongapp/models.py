from django.db import models

#세부지점에 대한 모델
class Spot(models.Model):
    #지점 이름
    name=models.CharField(max_length=20)

    #지점 사진
    #ImageField.height_field, ImageField.width_field로 이미지 사진을 제한가능
    picture=models.ImageField(blank=True)

    #지점 위치
    location=models.CharField(max_length=30)

    #date=models.DateFiled() <- 시간이 필요한가?

    #태그 1,2,3
    tag1=models.CharField(max_length=10)
    tag2=models.CharField(max_length=10)
    tag3=models.CharField(max_length=10)

    #지점 혼자별점(최대5점인 실수)
    star=models.FloatField(max_length=5)

    def __str__(self):
        return self.name
    

#Spot을 상속받는 식당클래스
class Restaurant(Spot):
    pass#식당만의 특이필드가 필요?