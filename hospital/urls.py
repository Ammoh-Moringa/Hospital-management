from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path





urlpatterns=[
    path("", views.index, name="index"),
    url('profile/',views.index,name='index'),
    url('register/',views.registration, name='registration'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path("patient/<str:pk>", views.patient, name="patient"),
]

