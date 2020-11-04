from django.urls import path

from cd_spec_viewer_web.cdspec import views

urlpatterns = [
    # /cdspec/
    path('', views.IndexView.as_view(), name='index'),
    # /cdspec/create/
    path('create/', views.create, name='create'),
    # /cdspec/<pk>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]