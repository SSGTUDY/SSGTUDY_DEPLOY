from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    email = models.EmailField(verbose_name = "email", max_length = 255, unique = True)
    name = models.CharField(max_length = 200, null = False, blank = True)
    nickname = models.CharField(max_length = 200, null = False, blank = False)
    phone_number = models.CharField(max_length=200, null = False, blank = False)
    address = models.CharField(max_length=200, null = True, blank = True)
    profile_image = models.ImageField(upload_to="profile/", blank = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nickname']

    def __str__(self):
        return "<%d %s>" %(self.pk, self.email)

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email :
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save (using = self._db)
        return user
    
    def create_user(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(email, password, **extra_fields)
