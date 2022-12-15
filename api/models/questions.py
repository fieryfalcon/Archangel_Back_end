from .user_participants import *
from django.contrib.postgres.fields import ArrayField


class section(models.Model):
    name_of_the_section = models.CharField(
        verbose_name="name of the section", max_length=50, unique=True)
    total_number_of_questions = models.IntegerField()
    total_marks = models.IntegerField()
    round_number = models.CharField(max_length=50)
    recruitment_season = models.ForeignKey(
        recruitment_season, on_delete=models.CASCADE)
    assignee_enrollment_number = models.ManyToManyField(
        "img_member", blank=True, null=True)

    class Meta:
        verbose_name = "section"
        verbose_name_plural = "sections"

    def __str__(self):
        return self.name_of_the_section


class Questions(models.Model):
    question_text = models.CharField(max_length=1000)
    answer_text = models.CharField(max_length=500)
    maximum_marks = models.IntegerField()
    difficulty = models.IntegerField()
    sectionID = models.ForeignKey(
        section, verbose_name="section of that question", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Questions"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text
