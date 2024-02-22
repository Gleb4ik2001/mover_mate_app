from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self,
        username=None,
        email = None,
        phone_number = None,
        password = None,
        **extra_fields
    ):
        pass

class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(
        verbose_name = 'почта',
        null = True,
        blank = True,
        unique = True
    )
    first_name = models.CharField(
        verbose_name = 'имя',
        max_length = 50,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        verbose_name = 'фамилия',
        max_length = 50,
        null=False,
        blank = False
    )
    phone_number= models.CharField(
        verbose_name = 'номер телефона',
        unique= True,
        max_length =12,
        null=False,
        blank = False
    )
    datetime_joined = models.DateTimeField(
        verbose_name = 'дата регистрации',
        auto_now_add = True
    )
    is_active = models.BooleanField(
        verbose_name = 'активный',
        default = False
    )
    is_staff = models.BooleanField(
        verbose_name = 'персонал',
        default = False
    )
    is_verified = models.BooleanField(
        verbose_name = 'верифицирован',
        default = False
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['phone_number']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering= ('-id',)
    
