# This test checks to see if the user's absolute url is correct 
# The assert statement checks if the user's absolute url is equal to the expected url 
 

from cd_spec_viewer_web.users.models import User

pytestmark = pytest.mark.django_db

# The test user_get_absolute_url checks to see if the user's absolute url is correct. import pytest
def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"
