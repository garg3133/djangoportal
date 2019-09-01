from django import forms

class UpdateForm(forms.Form):
    college = forms.CharField(label='College Name', max_length=50)