from django.urls import path

from .views import quistion, qiuz, users_upload, result_list

urlpatterns = [
    path('', qiuz, name='qiuz'),
    path('quiz/<int:pk>/', quistion, name='quistion'),
    path('users/', users_upload, name='users-upload'),
    path('results/<int:pk>/', result_list, name='result_detail'),
]