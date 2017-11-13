from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

# Import user authentication forms
from django.contrib.auth.forms import UserCreationForm

# Import Auth Models
from django.contrib.auth.models import User

# Import models
from .models import (Profile, Contractor, Project)

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    contractor = forms.ModelChoiceField(queryset=Contractor.objects.filter(is_active=True))

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =  ('construction_type', 'employer', 'consultant', 'status', 'full_name', 'short_name', 'description', 'contract_amount', 'signing_date', 'site_handover', 'commencement_date', 'period',)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
                    Fieldset(
                        'Project Summary',
                        'construction_type',
                        'employer',
                        'consultant',
                        'status',
                        'full_name',
                        'short_name',
                        'description',
                    ),
                    Fieldset(
                        'Contract Summary',
                        'contract_amount',
                        'signing_date',
                        'site_handover',
                        'commencement_date',
                        'period',
                    ),
                )
        super(ProjectForm, self).__init__(*args, **kwargs)