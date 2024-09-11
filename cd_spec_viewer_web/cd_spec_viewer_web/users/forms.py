"""Implements generic user creation and change forms
Globals:
    User
    
Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
"""
#Django
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    """Manages the user change form
    """
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    """Manages the  user creation form

    Inherited Attributes:
        error_messages: A dictionary containing error messages
        cleaned_data: A dictionary containing the desired username and both copies of the password entered
    """


    #Add custom error messages
    admin_forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    def clean_username(self) -> str:
        """Checks the database for duplicate users and returns a cleaned copy of the 
        username if it is unique.

        Returns:
            A cleaned copy of the username

        Raises:
            ValidationError: A duplicate username was found

        """
        username = self.cleaned_data["username"]

        try:
            #Attempt to lookup user
            User.objects.get(username=username)
        except User.DoesNotExist:
            #If user does not exist, return the username
            return username

        #If the lookup succeeded then the username is a duplicate
        raise ValidationError(self.error_messages["duplicate_username"])
