# Generated by Django 4.1.2 on 2022-12-15 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_recruitment_test_recruitment_season_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='connection_question_assignee',
        ),
    ]