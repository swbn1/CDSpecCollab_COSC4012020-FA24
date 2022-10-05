"""Custom views for users
Globals: 
    user_detail_view -> Model
    user_update_view -> Model
    user_redirect_view -> Model

Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
"""

#Django
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    """Displays a detailed view of the user's profile if they are authenticated
    Sends the user to the login page if not."""
    model = User
    #Existing data to be packaged with the URL
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Allows the user to edit their profile if they are authenticated
    Sends the user to the login page if not."""

    model = User
    fields = ["name"]

    def get_success_url(self):
        """Returns: URL to redirect the user to after the info is successfully updated"""
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        """Returns object representation of the current user"""
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        """Returns: HTTPResponse indicating the updated data has been received"""
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    """Either sends the user to their detailed view if they are authenticated
    Sends the user to the login page if not."""
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
