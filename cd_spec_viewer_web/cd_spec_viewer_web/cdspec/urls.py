
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




]