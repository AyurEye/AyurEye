from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

from django.contrib.auth.models import AbstractUser, UserManager



class AyurEyeUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        if not email:
            raise ValueError("Username must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email,username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email,username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email,username, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name= 'email address', unique=True, )
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(verbose_name="first name", max_length=150)
    last_name = models.CharField(verbose_name="last name", max_length=150)
    objects = AyurEyeUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    User_CHOICES = [
        ('Dr', 'Doctor'),
        ('Pt', 'Patient'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=2,
        choices=User_CHOICES,
        default='Pt',)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    license_photo = models.ImageField(upload_to='media/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    hospital_name = models.CharField(max_length=30, blank=True, null=True)






