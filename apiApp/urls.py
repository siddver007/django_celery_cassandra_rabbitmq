from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from apiApp.views import *

urlpatterns = [
    
    url(r'^$', registerView , name = 'register'),
    url(r'^post/$', csrf_exempt(postView.as_view()) , name = 'userPost'),
]
