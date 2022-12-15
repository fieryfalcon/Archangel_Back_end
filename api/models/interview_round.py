from random import choices
from django.db import models
from .user_participants import *


class interview_panels(models.Model):
    enrollment_number_1 = models.ManyToManyField(
        img_member, related_name='first')
    enrollment_number_2 = models.ManyToManyField(
        img_member, related_name='second')
    role = models.CharField(max_length=20)

    class Meta:
        verbose_name = "group_info"
        verbose_name_plural = "group_infos"

    def __str__(self):
        return self.role


class interview_section(models.Model):
    STATUS = (
        (1,  ('scheduled')),
        (2, ('not answered')),
        (3, ('pending'))
    )

    marks_obtained = models.IntegerField()
    enrollment_number = models.ForeignKey(
        Participants_detail, verbose_name="enrollment_number", on_delete=models.CASCADE)
    scheduling_status = models.PositiveSmallIntegerField(
        choices=STATUS, default=3)
    remarks = models.CharField(max_length=500)
    group_id = models.ForeignKey(
        interview_panels, verbose_name="interview panel", on_delete=models.CASCADE)
    round_number = models.CharField(max_length=20)
    date_and_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    recruitment_season_code = models.ForeignKey(
        recruitment_season, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "interview_section"
        verbose_name_plural = "interview_sections"

    def __str__(self):
        return self.group_id
