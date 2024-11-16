from django import forms
from .models import Participant
from django.contrib.auth.hashers import make_password

class ParticipantForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    gift_preference = forms.CharField(
        max_length=255,
        required=False,
        label='What do you want for Christmas?',
        widget=forms.TextInput(attrs={'placeholder': 'What would you like as a gift'})
    )

    class Meta:
        model = Participant
        fields = ['name', 'password', 'gift_preference']  # Include gift_preference

    def save(self, commit=True):
        participant = super().save(commit=False)
        # Hash the password before saving
        participant.password = make_password(self.cleaned_data['password'])
        if commit:
            participant.save()
        return participant