import pytest
from django.urls import resolve, reverse
from cd_spec_viewer_web.users.models import User

# marks the test as being run against a Django database
pytestmark = pytest.mark.django_db

def test_detail(user: User):
    # assertion that checks if the result of the reverse function is equal to the expected url for the detail view
    assert (
        reverse("users:detail", kwargs={"username": user.username})
        == f"/users/{user.username}/"
    )
    # assertion that checks if the result of the resolve function is equal to the expected view name for the detail view
    assert resolve(f"/users/{user.username}/").view_name == "users:detail"

def test_update():
    # assertion that checks if the result of the reverse function is equal to the expected url for the redirect view
    assert reverse("users:update") == "/users/~update/"
    # assertion that checks if the result of the resolve function is equal to the expected view name for the update view
    assert resolve("/users/~update/").view_name == "users:update"


def test_redirect():
    # assertion that checks if the result of the reverse function is equal to the expected url for the login view
    assert reverse("users:redirect") == "/users/~redirect/"
    # assertion that checks if the result of the resolve function is equal to the expected view name for the login view
    assert resolve("/users/~redirect/").view_name == "users:redirect"
