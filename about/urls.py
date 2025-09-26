
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.about_me, name='about'),
    path("accounts/", include("allauth.urls")),
]