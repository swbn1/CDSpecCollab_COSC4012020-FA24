"""Custom url pattern directives
Globals:
    app_name -> str
    urlpatterns -> path[]
Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
"""

#Django
from django.urls import path

#Local Django
from users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"), #/users/redirect/
    path("~update/", view=user_update_view, name="update"),       #/users/update/
    path("<str:username>/", view=user_detail_view, name="detail"),#/users/<username>
]
