from django.urls import path

from .views import social_account_login, return_fb_login

urlpatterns = [
    path('auth/', social_account_login, name='login'),
    path('callback/', return_fb_login, name='callback'),
]
