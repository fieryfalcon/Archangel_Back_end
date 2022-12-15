from random import choices
from django.db import models
from .user_participants import *


class recruitment_test(models.Model):
    STATUS = (
        (1,  ('verified')),
        (2, ('in progress')),
        (3, ('pending'))
    )
    enrollment_number = models.OneToOneField(
        "Participants_detail", on_delete=models.CASCADE)
    recruitment_season_code = models.ForeignKey(
        "recruitment_season",  on_delete=models.CASCADE)
    evaluation_status = models.PositiveSmallIntegerField(
        choices=STATUS, default=3)
    evaluation_result = models.CharField(max_length=50, null=True, blank=True)
    remarks = models.CharField(max_length=500, null=True, blank=True)
    total_marks = models.IntegerField(null=True, blank=True)
    evaluation_status = models.PositiveSmallIntegerField(
        choices=STATUS, default=3)

    class Meta:
        verbose_name = "recruitment_test"
        verbose_name_plural = "recruitment_tests"


class winter_assingment(models.Model):
    STATUS = (
        (1,  ('verified')),
        (2, ('in progress')),
        (3, ('pending'))
    )
    enrollment_number = models.OneToOneField(
        "Participants_detail", on_delete=models.CASCADE)
    recruitment_season_code = models.ForeignKey(
        "recruitment_season",  on_delete=models.CASCADE)
    project_link = models.URLField(max_length=200)
    evaluation_result = models.CharField(max_length=50, null=True, blank=True)
    remarks = models.CharField(max_length=500, null=True, blank=True)
    total_marks = models.IntegerField(null=True, blank=True)
    evaluation_status = models.PositiveSmallIntegerField(
        choices=STATUS, default=3)

    class Meta:
        verbose_name = "winter_assingment"
        verbose_name_plural = "winter_assingments"
