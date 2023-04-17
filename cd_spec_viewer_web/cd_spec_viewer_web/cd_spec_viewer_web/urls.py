"""cd_spec_viewer_web URL Configuration

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
    
    Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

    This file and all contributions herin are covered by the GPL 3.0 License 
    https://www.gnu.org/licenses/gpl-3.0.html
"""
#Django
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cdspec/', include('cdspec.urls')), #Configure CDSPEC app urls
    path('admin/', admin.site.urls),
    path("users/", include('users.urls')), #Configure USER app urls
    path("accounts/", include('allauth.urls')), #Configure urls from AllAuth
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path(
        "credits/", TemplateView.as_view(template_name="pages/credits.html"), name="credits"
    ),
    path(
        "", TemplateView.as_view(template_name="pages/home.html"), name="home"
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
