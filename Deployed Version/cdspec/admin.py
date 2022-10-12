"""Registers the admin model for the CDSpec app

Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
"""
#Django
from django.contrib import admin
#Local Django
from . import models

# Register your models here.
admin.site.register(models.SpecRun)
