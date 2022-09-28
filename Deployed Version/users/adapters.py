#commented by Andrew Kivrak
#importing any method from typing package
from typing import Any

#importing the required files from other package/classes(user defined)

#importing DefaultAccountAdapter from allauth.account.adapter
from allauth.account.adapter import DefaultAccountAdapter

#importing DefaultSocialAccountAdapter from allauth.socialaccount.adapter 
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

#importing settings form django.conf
from django.conf import settings

#importing HttpRequest from django.http 
from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):
    #creating a method to return attributes settings, ACCOUNT_ALLOW_REGISTRATION from the Account
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    #creating a method to return the attributes settings, ACCOUNT_ALLOW_REGISTRATION from socialAccount
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
