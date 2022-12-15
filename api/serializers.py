from pyexpat import model
from rest_framework import serializers

from .models import *


# serializer for img_member , recruitment season and participant_details

class img_member_serializer(serializers.ModelSerializer):
    class Meta:
        model = img_member
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


class recruitment_season_serializer(serializers.ModelSerializer):
    class Meta:
        model = recruitment_season
        fields = '__all__'


class participant_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Participants_detail
        fields = '__all__'

# class connection_participant_seasons_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = connection_participant_seasons
#         fields = '__all__'


# serializer for recruitment test and winter assignments

class recruitment_test_serializer(serializers.ModelSerializer):
    class Meta:
        model = recruitment_test
        fields = '__all__'


class winter_assingments_serializers(serializers.ModelSerializer):
    class Meta:
        model = winter_assingment
        fields = '__all__'


# serilaizer for interview rounds , interview panel

class interview_panel_serializer(serializers.ModelSerializer):
    class Meta:
        model = interview_panels
        fields = '__all__'


class interview_section_serializer(serializers.ModelSerializer):
    class Meta:
        model = interview_section
        fields = '__all__'


# serializer for questions , sections ,connection_assingee_question

class questions_serializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class sections_serializer(serializers.ModelSerializer):
    class Meta:
        model = section
        fields = '__all__'


# serializer for evalution and marks

class evaluation_serializer(serializers.ModelSerializer):
    class Meta:
        model = evaluation
        fields = '__all__'


class sectionwise_marks_serializer(serializers.ModelSerializer):
    class Meta:
        model = section_wise_marks
        fields = '__all__'
