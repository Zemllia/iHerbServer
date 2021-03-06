"""iHerbServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from .schema import CoreAPISchemaGenerator
import iHerbServer.api.v1.urls

urlpatterns = [
    path('', admin.site.urls),
    path('doc/', include_docs_urls(title='API', authentication_classes=[], permission_classes=[],
                                   generator_class=CoreAPISchemaGenerator)),
    path('api/v1/', include(iHerbServer.api.v1.urls.api_urlpatterns)),
    path('test/', include('allauth.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
]
