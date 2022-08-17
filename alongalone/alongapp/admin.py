from django.contrib import admin
from .models import Spot

# Register your models here.
#/admin사이트에서 spot클래스를 관리할수있도록 함
admin.site.register(Spot)
