from .user_participants import *
from .questions import *
from random import choices
from django.db import models


class evaluation(models.Model):
    enrollment_number = models.ForeignKey(
        Participants_detail, verbose_name="enroll. number", on_delete=models.CASCADE)
    Question_ID = models.ForeignKey(Questions, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    remarks = models.CharField(max_length=250)

    class Meta:
        verbose_name = "evaluation"
        verbose_name_plural = "evaluations"

    def int(self):
        return self.enrollment_number


class section_wise_marks(models.Model):
    evaluation_ID = models.ForeignKey(evaluation, on_delete=models.CASCADE)
    round_number = models.CharField(max_length=50)
    marks_in_the_section = models.IntegerField()
    section_name = models.ForeignKey(
        section, to_field="name_of_the_section", db_column="name_of_the_section", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "section_wise_mark"
        verbose_name_plural = "section_wise_marks"

    def __str__(self):
        return self.evaluation_ID
