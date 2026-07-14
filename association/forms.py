from django import forms
from .models import Complaint, Suggestion


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            'house_number',
            'name',
            'mobile_number',
            'complaint_category',
            'complaint_description',
            'photo'
        ]

        widgets = {
            'house_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter House Number'
            }),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name'
            }),

            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Mobile Number'
            }),

            'complaint_category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'complaint_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter Complaint Description'
            }),

            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = [
            'name',
            'mobile',
            'house_no',
            'email',
            'subject',
            'suggestion',
            'attachment'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name'
            }),

            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Mobile Number'
            }),

            'house_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter House Number'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email (Optional)'
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Subject'
            }),

            'suggestion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter Your Suggestion'
            }),

            'attachment': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Mandatory Fields
        self.fields['name'].required = True
        self.fields['mobile'].required = True
        self.fields['house_no'].required = True
        self.fields['subject'].required = True
        self.fields['suggestion'].required = True

        # Optional Fields
        self.fields['email'].required = False
        self.fields['attachment'].required = False