from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)

    fullname = models.CharField(max_length=255,null=True,blank=True)

    gender = models.CharField(max_length=255,null=True,blank=True)

    # 12/02/23
    

    city = models.CharField(max_length=255 , default='SOME STRING',null=True,blank=True)
    state = models.CharField(max_length=255, default='SOME STRING',null=True,blank=True)
    credit_num = models.IntegerField(null=True,blank=True)
    cvc = models.IntegerField(null=True,blank=True)

    expdate = models.DateField(null=True,blank=True)
    age = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=100,default="India")
    public_visibility = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = "username" # make the user log in with the email
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    

class Book(models.Model):
    # fk = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,null=True )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    file = models.FileField(blank=True, null=True)
    cover = models.ImageField(upload_to='cover/')
    pdf = models.FileField(upload_to='pdf/')

    def delete(self, *args, **kwargs):
        self.cover.delete()
        self.pdf.delete()
        super(Book, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title
    





