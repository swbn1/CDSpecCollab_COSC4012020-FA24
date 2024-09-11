"""This file contains all tests for views in the Users module

Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
"""
#Python
import pytest
#Django
from django.contrib.auth.models import AnonymousUser
from django.http.response import Http404
from django.test import RequestFactory
#Local modules
from cd_spec_viewer_web.users.models import User
from cd_spec_viewer_web.users.tests.factories import UserFactory
from cd_spec_viewer_web.users.views import (
    UserRedirectView,
    UserUpdateView,
    user_detail_view,
)

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def test_get_success_url(self, user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(self, user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user


class TestUserRedirectView:
    """Contains methods to test URL redirects"""
    def test_get_redirect_url(self, user: User, rf: RequestFactory):
        view = UserRedirectView()
        request = rf.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestUserDetailView:
    """Contains methods to test the user detail view"""
    def test_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = UserFactory() #Test with a fake valid user

        response = user_detail_view(request, username=user.username)
        #Confirm the request succeeded
        assert response.status_code == 200

    def test_not_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = AnonymousUser() #Test with a fake invalid user

        response = user_detail_view(request, username=user.username)
        #Confirm that the request fell through to login
        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/fake-url/"

    def test_case_sensitivity(self, rf: RequestFactory):

        request = rf.get("/fake-url/")
        request.user = UserFactory(username="UserName")
        #Navigate to detail page with incorrect capitalization
        with pytest.raises(Http404):
            user_detail_view(request, username="username")
            #TODO: Assert failure?
