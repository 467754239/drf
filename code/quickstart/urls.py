from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UserViewSet),
    url(r'^(?P<pk>[0-9]+)/$', views.GroupViewSet),
]