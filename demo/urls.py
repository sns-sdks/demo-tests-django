from django.urls import path

from .views import social_account_login, return_fb_login

urlpatterns = [
    path(r'^auth/$', social_account_login, name='login'),
    path(r'^callback/$', return_fb_login, name='callback'),
]
