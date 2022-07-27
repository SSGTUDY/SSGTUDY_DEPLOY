from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    username = models.CharField(max_length = 200, unique = True)
    nickname = models.CharField(max_length = 200, null = False, blank = False)
    phone_number = models.CharField(max_length=200, null = False, blank = False)
    profile_image = models.ImageField(upload_to="profile/", blank = True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname', 'phone_number', 'profile_image']

    def __str__(self):
        return "<%d %s>" %(self.pk, self.username)

class UserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username :
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username = username, **extra_fields)
        user.set_password(password)
        user.save (using = self._db)
        return user
    
    def create_user(self, username, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(username, password, **extra_fields)
