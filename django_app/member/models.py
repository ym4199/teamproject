from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, password):
        if not email:
            # email 를 등록 여부판단의 근거로 사용
            raise ValueError('Email 주소가 필요합니다!')

        user = self.model(
            email=email,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(email, nickname, password)
        user.is_admin = True
        user.is_superuser = True
        # 관리자 권한을 준다.
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    nickname = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=10)

    is_admin = models.BooleanField(default=False)
    # 기본적으로 false 를 부여하고 superuser가 변경가능

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    # createsuperuser 커맨드로 유저를 생성할 때 나타날 필드 이름 목록

    def get_nickname(self):
        return self.nickname

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.nickname

    def get_full_name(self):
        return self.email

    def get_username(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
