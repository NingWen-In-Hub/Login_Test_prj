from django import forms
from login_test_app.models import Profile


class AddForm2(forms.Form):
    test1 = forms.BooleanField(label='BooleanField2.0')
    CHOICES = (('1', 'ラーメン'), ('2', 'ソウメン'), ('3', 'イケメン'))
    test2 = forms.ChoiceField(label='ChoiceField', choices=CHOICES)


class NewForm2(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ()
