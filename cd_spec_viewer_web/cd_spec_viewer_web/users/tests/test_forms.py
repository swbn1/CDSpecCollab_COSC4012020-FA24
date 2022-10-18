import pytest   #Importing pytest library
#Below :- This line is importing UserCreationForm class from cd_spec_viewer_web.users.forms
from cd_spec_viewer_web.users.forms import UserCreationForm
#Below:- This line is importing UserFactory class from cd_spec_viewer_web.users.tests.factories
from cd_spec_viewer_web.users.tests.factories import UserFactory

#below line requesting the database access
'''
This is used to mark a test function as requiring the database. 
It will ensure the database is set up correctly for the test.
'''
pytestmark = pytest.mark.django_db

#Below is defining class
class TestUserCreationForm:
    #method initilization under class
    def test_clean_username(self):
        # A user with proto_user params does not exist yet.
        """
        this  function is determining whether
        username is in the proper format or not
        if it is then it throw assertion in program
        """

        #This line is initilizing an object of UserFactory class which are calling build method
        proto_user = UserFactory.build()

        #Below line is creating an object od UserCreationForm whith parameterized constructor calling
        form = UserCreationForm(
        {
        "username": proto_user.username,  #username is assigned proto_user.name
        "password1": proto_user._password, #password1 is assigned proto_user.password
        "password2": proto_user._password,  #password2 is assigned proto_user.password
        }
        )

        """
        Below two lines throw assertion if any of return false
        """
        assert form.is_valid()  #Checking if form contain valid data
        assert form.clean_username() == proto_user.username  #Checking if username is in proper format or not


        # Creating a user.
        form.save()

    # The user with proto_user params already exists,
    # hence cannot be created.
        form = UserCreationForm(
        {
        "username": proto_user.username,
        "password1": proto_user._password,
        "password2": proto_user._password,
        }
        )

        assert not form.is_valid()  #if form is not valid then throwing assertion
        assert len(form.errors) == 1  #If form contain any error then throw assertion
        assert "username" in form.errors   #If username contain error then throw assertion
