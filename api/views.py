from math import perm
import this
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
import requests
from django.shortcuts import redirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from rest_framework.filters import *
from django_filters.rest_framework import DjangoFilterBackend


from http import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .permissions import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt


# viewsets for participants detail and user details


def authorise(request):
    x = request.method
    redirect_url = "https://channeli.in/oauth/authorise/?client_id=N3MPpGh1CNcZ4nUY02LXl5RwzjbrJaVLmJxSCiYU&redirect_uri=http://127.0.0.1:8000/user/login/&state=RANDOM_STATE_STRING"
    if x == 'GET':
        response = redirect(redirect_url)
        return response


def authorise2(request):

    authorisation_code = request.GET.get("code")
    object = {"client_id": "N3MPpGh1CNcZ4nUY02LXl5RwzjbrJaVLmJxSCiYU", "client_secret": "DdeHkCStAaH2vfnixxe3FRWzI9wfyx26dKCeK8jdeN6ftqdUwbgU3fV0DDVggpygRWRfOGr4Cxb7njC3gqbgeTOkaAsn0piv4i40E4acRudZhYTPOkiDLmiZCAKgMdoM",
              "grant_type": "authorization_code", "redirect_uri": "http://127.0.0.1:8000/user/login/",
              "code": authorisation_code}
    json_response = requests.post(
        "https://channeli.in/open_auth/token/", data=object)
    json_data = json_response.json()
    user_json = requests.get(url="https://channeli.in/open_auth/get_user_data/",
                             headers={"Authorization": f"Bearer {json_data['access_token']}"})
    user_data = user_json.json()

    global year
    global token

    Img = user_data["person"]["roles"][1]["role"]
    enrollment_number = int(user_data["username"])
    name = str(user_data["person"]["fullName"])
    year = user_data["student"]["currentYear"]
    email = user_data["contactInformation"]["instituteWebmailAddress"]

    data = {
        'name': f'{name}',
        'enrollment_number': f'{enrollment_number}',
        'year': f'{year}',

    }

    user = img_member.objects.filter(
        enrollment_number=enrollment_number).exists()
    token = Token.objects.filter(user=request.user.enrollment_number)

    if Img == 'Maintainer':

        if user:
            user = img_member.objects.get(enrollment_number=enrollment_number)
            login(request, user)

            user_data["token"] = Token.objects.get(user=user).key
            return redirect(f'http://localhost:3000/loading/?token={user_data["token"]}&year={year}')

        else:

            user = img_member.objects.create_normal_user(
                enrollment_number=enrollment_number,
                email=email,
                name=name,
                year=year,
            )

            user.save()
            user = img_member.objects.get(enrollment_number=enrollment_number)
            login(request, user)
            return redirect(f'http://localhost:3000/loading/?token={user_data["token"]}')
    else:
        return HttpResponse("not an IMG member")


class img_member_viewset(viewsets.ModelViewSet):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = img_member.objects.all()
    serializer_class = img_member_serializer
    filterset_fields = ['year']
    filter_backends = [DjangoFilterBackend]


class recruitment_season_viewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, can_3y_and_2y_view]
    queryset = recruitment_season.objects.all()
    serializer_class = recruitment_season_serializer

    # @action(detail=False, methods=['POST'], permission_classes=[Not_2y])
    # def create_paper(self, request):
    #     if request.user.year > 3:
    #         year = request.data['year']
    #         role = request.data['role']
    #         ques = recruitment_season(year=year, role=role)
    #         ques.save()
    #     return HttpResponse("Done")


class participant_detail_viewset(viewsets.ModelViewSet):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [Not_2y, IsAuthenticated]
    queryset = Participants_detail.objects.all()
    serializer_class = participant_detail_serializer
    # filterset_fields = ['recruitment_season_code']
    # filter_backends = [DjangoFilterBackend]

    # @action(detail=False, methods=['GET'], permission_classes=[Not_2y])
    # def create_paper(self, request):

    #     recruitment_season_code = request.data("code")
    #     return Participants_detail.objects.filter(name="vaish")

    # if request.user.year > 1:

    #     recruitment_season_code = request.data("code")
    #     enrollment_number = request.data("enrollment_number")
    #     object = {"Participants_detail": enrollment_number,
    #               "recruitment_season_code": recruitment_season_code}
    #     json_response2 = requests.post(
    #         "http://localhost:8000/user/api_view/connection_participant_season/", data=object).json()

    # return HttpResponse(json_response2)

    # def set_password(self, request):

    #     recruitment_season_code = request.data("code")
    #     enrollment_number = request.data("enrollment_number")
    #     object = {"Participants_detail": enrollment_number,
    #               "recruitment_season_code": recruitment_season_code}
    #     json_response2 = requests.post(
    #         "http://localhost:8000/user/api_view/connection_participant_season/", data=object).json()

    #     return HttpResponse(json_response2)


# class connection_participant_seasons_viewset(viewsets.ModelViewSet):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [Not_2y, IsAuthenticated]
#     queryset = connection_participant_seasons.objects.all()
#     serializer_class = connection_participant_seasons_serializer

    # @action(detail=False, methods=['POST'], permission_classes=[Not_2y])
    # def create_paper(self, request):
    #     if request.user.year > 1:

    #         recruitment_season_code = request.data("code")
    #         enrollment_number = request.data("enrollment_number")
    #         object = {"Participants_detail": enrollment_number,
    #                   "recruitment_season_code": recruitment_season_code}
    #         json_response2 = requests.post(
    #             "http://localhost:8000/user/api_view/connection_participant_season/", data=object).json()

    #     return HttpResponse(json_response2)


class section_viewset(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [Not_2y, IsAuthenticated]
    queryset = section.objects.all()
    serializer_class = sections_serializer


class Questions_viewset(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [Not_2y, IsAuthenticated]
    queryset = Questions.objects.all()
    serializer_class = questions_serializer
    filterset_fields = ['sectionID']
    filter_backends = [DjangoFilterBackend]


class recruitment_test_viewset(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [Not_2y, IsAuthenticated]
    queryset = recruitment_test.objects.all()
    serializer_class = recruitment_test_serializer
    filterset_fields = ['recruitment_season_code']
    filter_backends = [DjangoFilterBackend]


class winter_assingment_viewset(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [Not_2y, IsAuthenticated]
    queryset = winter_assingment.objects.all()
    serializer_class = winter_assingments_serializers
    filterset_fields = ['recruitment_season_code']
    filter_backends = [DjangoFilterBackend]


class evaluation_viewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Not_2y, IsAuthenticated]
    queryset = evaluation.objects.all()
    serializer_class = evaluation_serializer


class section_wise_marks_viewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Not_2y, IsAuthenticated]
    queryset = section_wise_marks.objects.all()
    serializer_class = sectionwise_marks_serializer


class interviewsection_viewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = interview_section.objects.all()
    serializer_class = interview_section_serializer


class interview_panel_viewset(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [can_3y_and_2y_view, IsAuthenticated]
    queryset = interview_panels.objects.all()
    serializer_class = interview_panel_serializer
