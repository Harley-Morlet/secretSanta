from django.contrib import admin
from django import forms
from django.contrib.auth.hashers import make_password
from django.forms import PasswordInput
from .models import Participant

class ParticipantAdminForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput, label='Password', required=False)

    class Meta:
        model = Participant
        fields = ['name', 'assigned_name', 'password', 'signup_date']

    def save(self, commit=True):
        participant = super().save(commit=False)
        # Only hash the password if it's changed
        if self.cleaned_data['password']:
            participant.password = make_password(self.cleaned_data['password'])
        if commit:
            participant.save()
        return participant

class ParticipantAdmin(admin.ModelAdmin):
    form = ParticipantAdminForm

admin.site.register(Participant, ParticipantAdmin)