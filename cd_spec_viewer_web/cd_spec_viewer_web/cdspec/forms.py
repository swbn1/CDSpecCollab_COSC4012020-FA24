from django import forms
from django.forms import ModelForm
from cd_spec_viewer_web.cdspec.models import SpecRun

AXIS_CHOICES = [('nanometers', 'nm'), ('degrees', 'mdeg'), ('voltage', 'V'), ('absorbance', 'absorbance')]
AXIS_CHOICES_WITH_NONE = AXIS_CHOICES + [('None', 'None')]

#Upload form, model specifies which database table to use and fields specify the fields included in the form.
class CreateForm(ModelForm):
    class Meta:
        model = SpecRun
        fields = ('run_title', 'run_description', 'run_user', 'visible_student', 'visible_public',
         'source_file', 'protein_concentration', 'pathlength', 'number_of_amino_acids')

class EditForm(ModelForm):
    class Meta:
        model = SpecRun
        fields = ('run_title', 'run_description', 'visible_student', 'visible_public')

class AxesForm(forms.Form):
    x_axis = forms.ChoiceField(label="X Axis", choices=AXIS_CHOICES, initial='nanometers')
    y_axis = forms.ChoiceField(label="Y Axis", choices=AXIS_CHOICES, initial='degrees')
    z_axis = forms.ChoiceField(label="Z Axis", choices=AXIS_CHOICES_WITH_NONE, initial='None')