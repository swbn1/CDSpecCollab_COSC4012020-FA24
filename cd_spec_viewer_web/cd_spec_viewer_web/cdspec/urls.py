from django.urls import path, re_path

from cd_spec_viewer_web.cdspec import views


app_name = 'cdspec'

urlpatterns = [
    # /cdspec/
    path('', views.IndexView.as_view(), name='index'),
    # /cdspec/create/
    path('create/', views.create, name='create'),
    # /cdspec/<pk>/
    path('<int:pk>/', views.detail, name='detail'),
    #/cdspec/<pk>/edit
    path('<int:pk>/edit/', views.edit, name='edit'),
    #/cdspec/multi/<pk>/<pk>/ with unlimited <pk>'s, they must all be valid
    re_path('^multi/(?P<pks>(?:[1-9][0-9]*/)+)$', views.multi, name='multi')




]