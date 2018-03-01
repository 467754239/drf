"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views

from rest_framework import routers
from quickstart.views import UserViewSet, GroupViewSet


'''
Routers
    URL pattern: ^users/$ Name: 'user-list'
    URL pattern: ^users/{pk}/$ Name: 'user-detail'
    URL pattern: ^accounts/$ Name: 'account-list'
    URL pattern: ^accounts/{pk}/$ Name: 'account-detail' 
'''
'''quickstart'''
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^snippets/', include('snippets.urls')),
    url(r'^accounts/', include('accounts.urls')),

    # 用户获取token
    url(r'^api-token-auth/', views.obtain_auth_token),
]


urlpatterns += router.urls

