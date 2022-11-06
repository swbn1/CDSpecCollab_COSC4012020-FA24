"""This file specifies valid URL patterns for viewing CDSpec models

Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
"""
from django.urls import path, re_path
from django.conf.urls import url
#IMPORT DISCREPANCY: These 2 not imported on deployed folder variant
from django.contrib import admin
from django.urls import path, include # <--

#IMPORT DISCREPANCY: This 1 not same path as deployed version
from cd_spec_viewer_web.cdspec import views
from .views import SpecRunJson

app_name = 'cdspec'

urlpatterns = [
    # /cdspec/
    path('', views.IndexView.as_view(), name='index'),
    # CODE DISCREPANCY: This path not included but included on deployed:
    # /cdspec/uploadedby=<username>/
    # path('uploadedby=<str:user>/', views.IndexView.as_view(), name='userindex'),
    # /cdspec/create/
    path('create/', views.create, name='create'),
    # /cdspec/<pk>/
    path('<int:pk>/', views.detail, name='detail'),
    #/cdspec/<pk>/edit
    path('<int:pk>/edit/', views.edit, name='edit'),
    #/cdspec/<pk>/delete POST only
    path('<int:pk>/delete/', views.delete, name='delete'),
    #/cdspec/multi/<pk>/<pk>/ with unlimited <pk>'s, they must all be valid
    re_path('^multi/(?P<pks>(?:[1-9][0-9]*/)+)$', views.multi, name='multi'),
    # /cdspec/ table data
    url(r'^spec_run_data/$', SpecRunJson.as_view(), name="spec_run_list_json"),
    # CODE DISCREPANCY: Contains these 2 paths, but doesn't include additinal path from deployed (commented it in)
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('spec_run_data/<str:user>/', SpecRunJson.as_view(), name="spec_run_list_json_user"),
]
