import pytest

from cd_spec_viewer_web.users.models import User
from cd_spec_viewer_web.users.tests.factories import UserFactory

#tmpdir - provides a py.path.local object to a temporary directory which is unique to each test function; replaced by tmp_path


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    """ Set the media root to a temporary folder. """
    settings.MEDIA_ROOT = tmpdir.strpath

@pytest.fixture
def user() -> User:
    return UserFactory()
