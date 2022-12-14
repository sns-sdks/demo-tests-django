from django.conf import settings
from django.shortcuts import redirect, reverse
from django.http.response import JsonResponse
from pyfacebook import GraphAPI


def social_account_login(request):
    social_account_parameter = request.GET.get('social_account')
    # FB case
    if social_account_parameter == 'FB':
        redirect_uri = settings.DOMAIN_URL + reverse('return_fb_login')
        api = GraphAPI(app_id=settings.FB_APP_ID, app_secret=settings.FB_APP_SECRET, oauth_flow=True)
        auth_url = api.get_authorization_url(redirect_uri=redirect_uri, scope=['pages_show_list'])

        return redirect(auth_url[0])
    # If there's an invalid parameter return error
    else:
        return JsonResponse({'Error': f'Social account parameter {social_account_parameter} not valid'})


def return_fb_login(request):
    redirect_uri = settings.DOMAIN_URL + reverse('return_fb_login')
    response_uri = settings.DOMAIN_URL + reverse('return_fb_login') + '?code=' + request.GET['code']
    api = GraphAPI(app_id=settings.FB_APP_ID, app_secret=settings.FB_APP_SECRET, application_only_auth=True)
    token = api.exchange_user_access_token(response=response_uri, redirect_uri=redirect_uri)
    return JsonResponse(token, safe=False)
