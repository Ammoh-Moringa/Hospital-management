from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views





urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('register/',views.registration, name='registration'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
]

