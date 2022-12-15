
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('img_member', views.img_member_viewset, basename='season')
router.register('recruitment_season',
                views.recruitment_season_viewSet, basename='recruitment_season')
router.register('Participants_detail',
                views.participant_detail_viewset, basename='Participants_detail')
router.register('recruitment_test', views.recruitment_test_viewset,
                basename='recruitment_test')
router.register('winter_assingment',
                views.winter_assingment_viewset, basename='winter_assingment')
router.register('interview_panels', views.interview_panel_viewset,
                basename='interview_panels')
router.register('interview_section',
                views.interviewsection_viewset, basename='interview_section')
router.register('Questions', views.Questions_viewset, basename='Questions')
router.register('section', views.section_viewset, basename='section')
router.register('section_wise_marks',
                views.section_wise_marks_viewset, basename='section_wise_marks')

router.register('evaluation', views.evaluation_viewset, basename='evaluation')
# router.register('connection_participant_season',
#                 views.connection_participant_seasons_viewset, basename='connection_participant_season')

urlpatterns = [
    path('', views.authorise, name="getting_token"),
    path('login/', views.authorise2, name="authorise 2"),
    path('api_view/', include(router.urls)),



]
