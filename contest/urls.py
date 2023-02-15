from django.urls import path
from .views import ContestList, DetailContest
urlpatterns = [
    path('',ContestList.as_view(), name='contest_list'),
    path('contest/<int:pk>/', DetailContest.as_view(), name='contest_detail')
]