import datetime
from enum import unique
from inspect import _void
from django.db import models
from django.contrib.auth.models import *
from random import choices
import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


def year_choices():
    return [(r, r) for r in range(datetime.date.today().year-2, datetime.date.today().year+4)]


def current_year():
    return datetime.date.today().year


class img_member_manager(BaseUserManager):

    def create_normal_user(self, enrollment_number, name, year, email, password=None):
        if not enrollment_number:
            raise ValueError("User must have a enrollment number")
        if not name:
            raise ValueError("User must have a name")
        if not year:
            raise ValueError("User must have a year")
        if not email:
            raise ValueError("User must have a email")

        user = self.model(email=self.normalize_email(email))
        user.enrollment_number = enrollment_number
        user.name = name
        user.year = year

        def user_creation(self, user):
            self.user = user
            user.active = True
            user.set_password(password)
            user.save(using=self._db)

        if year == 2:
            user.admin = False
            user.staff = False

        user_creation

        if year == 4:
            user.admin = True
            user.staff = True

        user_creation

        if year == 3:
            user.admin = False
            user.staff = True

        user_creation

        return user

    def superuser_status(self, enrollment_number, name, year, email, password):

        user = self.create_normal_user(

            enrollment_number,
            password=password,
            name=name,
            year=year,
            email=email,


        )

        user.active = True
        user.admin = True
        user.staff = True

        user.save()
        return user


class img_member(AbstractBaseUser):
    name = models.CharField(max_length=70)
    year = models.IntegerField()
    is_designer = models.BooleanField(default=True, null=True)
    enrollment_number = models.IntegerField(primary_key=True, unique=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = "enrollment_number"
    REQUIRED_FIELDS = ["email", "name", "year"]

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    objects = img_member_manager()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class recruitment_season(models.Model):
    STATUS = (
        (1,  ('development')),
        (2, ('design')),
    )
    role = models.PositiveIntegerField(choices=STATUS, default=1)
    year = models.IntegerField(choices=year_choices(), default=current_year())

    class Meta:
        verbose_name = "recruitment_season"
        verbose_name_plural = "recruitment_seasons"

    def int(self):
        return self.year


class Participants_detail(models.Model):
    STATUS = (
        (1,  ('recruitment Test')),
        (2, ('Winter Assingment')),
    )
    enrollment_number = models.IntegerField(primary_key=True, unique=False)
    name = models.CharField(max_length=40)
    department = models.CharField(max_length=50)
    mode_of_entry = models.PositiveSmallIntegerField(choices=STATUS, default=1)
    phone_number = models.BigIntegerField(("phone number"), default=123456789)
    email = models.EmailField(("email"), max_length=254, null="True")
    recruitment_season_code = models.ManyToManyField("recruitment_season")
    Project_link = models.CharField(
        max_length=200, null=True, default="", blank=True)

    class Meta:
        verbose_name = "Participants_detail"
        verbose_name_plural = "Participants_details"

    def __str__(self):
        return self.name
