from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
"""
User커스텀 클래스
하는이유: 장고에서 기본으로 제공하는 User클래스는 커스텀하는데 한계가 있음.

필드:
0~5는 회원가입할때 입력받을것임
0. 비밀번호
1. 유저아이디(고유pk)
3. 이름(==닉네임)
4. 프로필사진
5. 대표카테고리(변경가능해야함)
6. 내소개
7. 얼롱캐쉬(이름은 새싹)
    구현미확정:
    7. 팔로워 목록
    8. 팔로우 목록
"""

CATEGORY = (
    ("b", "혼밥"),
    ("s", "혼술"),
    ("c", "혼카페")
)

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            password=password,
            username=username
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#아래 참조
#https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.FileField.upload_to
def profilePhoto_path(instance, filename):
    ext=filename.split(".")[-1]
    return "profilephoto/{}.{}".format(instance.username, ext)

class User(AbstractBaseUser):
    username = models.CharField(max_length=20, primary_key=True)
    nickname = models.CharField(max_length=20, blank=True)
    profilePhoto = models.ImageField(
        upload_to=profilePhoto_path,
        default="accountapp/static/img/default_user.png"
    )
    mainCategory = models.CharField(
        choices=CATEGORY,
        default="b",
        max_length=100
    )
    introduction = models.CharField(max_length=100, blank=True)
    cash = models.PositiveIntegerField(default=0)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'user'
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
