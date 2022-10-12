"""Implements the generic forms for viewing CDSpec models

Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
"""
#Django
from django.forms import ModelForm
from cdspec.models import SpecRun



#Upload form, model specifies which database table to use and fields specify the fields included in the form.
class CreateForm(ModelForm):
    class Meta:
        model = SpecRun
        fields = ('run_title', 'run_description', 'run_user', 'visible_student', 'visible_public',
         'source_file', 'protein_concentration', 'pathlength', 'number_of_amino_acids')
#Edit Form, fields specify the fields that can be edited
class EditForm(ModelForm):
    class Meta:
        model = SpecRun
        fields = ('run_title', 'run_description', 'visible_student', 'visible_public')
