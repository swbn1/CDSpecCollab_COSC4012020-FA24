from django.urls import path

from cd_spec_viewer_web.cdspec import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
    
]