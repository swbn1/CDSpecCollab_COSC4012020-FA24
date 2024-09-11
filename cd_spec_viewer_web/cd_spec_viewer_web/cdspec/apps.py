"""Declares the CdSpec AppConfig

Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
"""
#Django
from django.apps import AppConfig

#'CDspecConfig' is a subclass of classs 'AppConfig'
class CdspecConfig(AppConfig):

   """Configures the CDspece app""" 

   name = 'cdspec'

