import uuid
import jwt
import random

from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from rest_framework_jwt.utils import jwt_payload_handler

# from .utils import *

# Create your models here.

class MyUserManager(BaseUserManager):

    def create_superuser(self, user_name, password):
        user = self.model(user_name=user_name)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_user(self, user_name, password=None, username=''):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not user_name:
            raise ValueError('Users must have an user name')

        user = self.model(
            user_name=self.user_name,
            is_active=False,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class MyUsers(AbstractBaseUser):
	"""
		User information
	"""
	TYPE_OF_ACCOUNT = (
        ("Public", "Public"),
        ("Private", "Private"),
    )
	DEVICE_TYPE = (
		("Ios","Ios"),
		("Android","Android"),
	)
	SOCIAL_TYPE = (
		("Facebook","Facebook"),
		("Google","Google"),
	)
	country_code = models.CharField(
		"country Code", max_length=10, blank=True, null=True
	)
	email_address = models.EmailField(
		"Email Address", unique=True, max_length=50, null=True, blank=True
	)
	mobile_number = models.CharField(
		"Mobile Number", max_length=16, blank=True, null=True
	)
	mobile_number_verify = models.BooleanField(
		"Mobile number verify", default=False
	)
	name = models.CharField(
        "Name", max_length=100, blank=True, null=True
    )
	uuid = models.UUIDField(
        default=uuid.uuid4, editable=False
    )
	user_name = models.TextField(
    	"User Name", unique=True
	)
	accepting_terms = models.BooleanField(
        "Terms & Condition", default=False
    )
	device_id = models.TextField(
    	"Device id"
	)
	about_me = models.TextField(
		"About me", blank=True, null=True
	)
	age = models.IntegerField(
		"Age", default=0
	)
	gender = models.CharField(
		"Gender", max_length=20, blank=True, null=True
	)
	image = models.TextField(
		"image", blank=True, null=True
	)
	device_type = models.CharField(
		"Device Type", max_length=20, choices=DEVICE_TYPE, default="Android"
	)
	social_type = models.CharField(
		"Social Type", max_length=30,choices=SOCIAL_TYPE, default="Google"
	)
	type_of_Account = models.CharField(
		"Type of Account", default="Public", max_length=20, choices=TYPE_OF_ACCOUNT
	)
	is_superuser = models.BooleanField(
        "Super User", default=False
    )
	is_staff = models.BooleanField(
        "Staff", default=False
    )
	is_active = models.BooleanField(
        "Status", default=False
    )
	otp = models.CharField(
		"OTP",blank=True, null=True, max_length=7
	)
	is_online = models.BooleanField(
		"User is online", default=False
	)
	created_at = models.DateTimeField(
        "Created Date", auto_now_add=True
    )
	updated_at = models.DateTimeField(
        "Updated Date", auto_now=True
    )

	objects = MyUserManager()
	USERNAME_FIELD = 'user_name'

	def has_perm(self, perm, obj=None):
	    return self.is_staff

	def has_module_perms(self, app_label):
	    return self.is_superuser

	def get_short_name(self):
	    return self.user_name

	# def create_jwt(self):
	# 	"""Function for creating JWT for Authentication Purpose"""
	# 	payload = jwt_payload_handler(self)
	# 	token =  jwt.encode(payload, settings.SECRET_KEY)
	# 	auth_token = token.decode('unicode_escape')
	# 	return auth_token

	def __str__(self):
	    return self.user_name

	class Meta:
	    verbose_name = "User"
	    verbose_name_plural = "User"
