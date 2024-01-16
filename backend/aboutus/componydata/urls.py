from django.urls import path
from . import views


urlpatterns=[
    path('/int:pk/',views.MydataDetailAPIView.as_view()),
    path('/update/int:pk/',views.MydataUpdateAPIView.as_view()),
]