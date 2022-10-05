"""Configures the automatic admin interface
Globals:
    User (Also defined in forms.py, Duplicate?)

Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
"""
#Commented by Andrew Kivrak
#Django
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
#Local Django
from users.forms import UserChangeForm, UserCreationForm


# Create a user model object with the name User and register User in the admin.
User = get_user_model()
@admin.register(User)

# Create a UserAdmin class. This class will contain the interface operations to the User model. 

# form -> Logout current User and login another User
# add_form -> Add new User
class UserAdmin(auth_admin.UserAdmin):
    """Custom implementation of the UserAdmin class from Django.auth
    Similar solution with explination: https://stackoverflow.com/questions/15012235/using-django-auth-useradmin-for-a-custom-user-model"""
    form = UserChangeForm #override the form used to modify items
    add_form = UserCreationForm #override the form used to create items
    fieldsets = tuple(
        auth_admin.UserAdmin.fieldsets
    )

    # Define the structure and fields of the user model.
    staff_fieldsets = (
        (None, {'fields': ("username", "is_staff")}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Define which fields are to be made Read-Only to the staff in a tuple.
    staff_readonly_fields = ('name', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')
 
    # Define which fields are to be used while displaying list of staff in a list.
    list_display = ["username", "name", "is_superuser"]
    
    # Define which field can be used to search for a user in a list.
    search_fields = ["name"]

    # Define a function get_fieldsets. This method will return data field values from the User Model.
    def get_fieldsets(self, request, obj=None):
        # If the user is not a superuser, return the data of the user in staff_fieldsets.
        if not request.user.is_superuser:
            return self.staff_fieldsets
        # If the user is a superuser, return the data of all users.
        else:
            return super(UserAdmin, self).get_fieldsets(request, obj)

    # Define a function get_readonly_fields. This method will return all readonly data field values from the User Model.
    def get_readonly_fields(self, request, obj=None):
        # If the user is not a superuser, return the readonly data of the user in staff_readonly_fields.
        if not request.user.is_superuser:
            return self.staff_readonly_fields
        # If the user is a superuser, return the data of all users.
        else:
            return super(UserAdmin, self).get_readonly_fields(request, obj)
