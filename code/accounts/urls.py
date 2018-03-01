from django.conf.urls import url
from .views import GenToken, UserApiView


urlpatterns = [
    url(r'^try_user_auth/$', UserApiView.as_view()),
    url(r'^auth/token/$', GenToken.as_view()),
]