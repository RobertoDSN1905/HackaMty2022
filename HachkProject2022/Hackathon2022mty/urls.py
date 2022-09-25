from django.urls import path
from .views import HomePageView,LoginPageView
#from django.contrib import admin

urlpatterns = [
    path('',LoginPageView.as_view(),name="login"),
    path('analytics',HomePageView.as_view(),name="index")
]
