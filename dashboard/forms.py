from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

# Import user authentication forms
from django.contrib.auth.forms import UserCreationForm

# Import Auth Models
from django.contrib.auth.models import User

# Import models
from .models import (Profile, 
                     Contractor, 
                     Project, 
                     Insurance, 
                     Variation, 
                     Claim,)

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    title = forms.CharField(label='Job Title', max_length=100)
    contractor = forms.ModelChoiceField(queryset=Contractor.objects.filter(is_active=True))

    def __init__(self, *args, **kwargs):
      super(SignupForm, self).__init__(*args, **kwargs)
      self.fields['password1'].help_text = ''

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('title', 'bio')

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

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance 
        fields = ('project', 'insurance_type', 'bank', 'amount', 'start_date', 'period', 'status', 'issue_number', 'description',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(InsuranceForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(contractor=user.profile.contractor)

class VariationForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields =  ('project', 
                   'activity', 
                   'title', 
                   'work_order', 
                   'status', 
                   'description', 
                   'received_date', 
                   'received_letter',
                   'submitted_date', 
                   'submitted_letter', 
                   'submitted_amount', 
                   'approved_date', 
                   'approved_letter', 
                   'approved_amount', 
                   'remark',)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
                    Fieldset(
                        'Variation Summary',
                        'project',
                        'activity',
                        'title',
                        'work_order',
                        'description',
                        'received_date',
                        'received_letter',
                        'status',
                        'remark',
                    ),
                    Fieldset(
                        'Submittal Summary',
                        'submitted_amount',
                        'submitted_date',
                        'submitted_letter',                        
                    ),
                    Fieldset(
                        'Approval Summary',
                        'approved_amount',
                        'approved_date',
                        'approved_letter',                        
                    ),
                )
        user = kwargs.pop('user')
        super(VariationForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(contractor=user.profile.contractor)

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields =  ('project',
                   'title', 
                   'description',
                   'status', 
                   'remark',
                   'submitted_date', 
                   'submitted_letter', 
                   'submitted_amount', 
                   'approved_date', 
                   'approved_letter', 
                   'approved_amount',)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
                    Fieldset(
                        'Time Claim Summary',
                        'project',
                        'title',
                        'description',
                        'status',
                        'remark',
                    ),
                    Fieldset(
                        'Submittal Summary',
                        'submitted_amount',
                        'submitted_date',
                        'submitted_letter',                        
                    ),
                    Fieldset(
                        'Approval Summary',
                        'approved_amount',
                        'approved_date',
                        'approved_letter',                        
                    ),
                )
        user = kwargs.pop('user')
        super(ClaimForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(contractor=user.profile.contractor)

class ProjectVariationForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields =  ('activity', 
                   'title', 
                   'work_order', 
                   'status', 
                   'description', 
                   'received_date', 
                   'received_letter',
                   'submitted_date', 
                   'submitted_letter', 
                   'submitted_amount', 
                   'approved_date', 
                   'approved_letter', 
                   'approved_amount', 
                   'remark',)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
                    Fieldset(
                        'Variation Summary',
                        'activity',
                        'title',
                        'work_order',
                        'description',
                        'received_date',
                        'received_letter',
                        'status',
                        'remark',
                    ),
                    Fieldset(
                        'Submittal Summary',
                        'submitted_amount',
                        'submitted_date',
                        'submitted_letter',                        
                    ),
                    Fieldset(
                        'Approval Summary',
                        'approved_amount',
                        'approved_date',
                        'approved_letter',                        
                    ),
                )
        super(ProjectVariationForm, self).__init__(*args, **kwargs)

class ProjectClaimForm(forms.ModelForm):
            class Meta:
                model = Claim
                fields =  ('title', 
                           'description',
                           'status', 
                           'remark',
                           'submitted_date', 
                           'submitted_letter', 
                           'submitted_amount', 
                           'approved_date', 
                           'approved_letter', 
                           'approved_amount',)

            def __init__(self, *args, **kwargs):
                self.helper = FormHelper()
                self.helper.form_tag = False
                self.helper.layout = Layout(
                            Fieldset(
                                'Time Claim Summary',
                                'title',
                                'description',
                                'status',
                                'remark',
                            ),
                            Fieldset(
                                'Submittal Summary',
                                'submitted_amount',
                                'submitted_date',
                                'submitted_letter',                        
                            ),
                            Fieldset(
                                'Approval Summary',
                                'approved_amount',
                                'approved_date',
                                'approved_letter',                        
                            ),
                        )
                super(ProjectClaimForm, self).__init__(*args, **kwargs)