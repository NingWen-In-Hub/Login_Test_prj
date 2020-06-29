from django import forms


class AddForm2(forms.Form):
    test1 = forms.BooleanField(label='BooleanField3.0')
    CHOICES = (('1', 'ラーメン'), ('2', 'ソウメン'), ('3', 'イケメン'))
    test2 = forms.ChoiceField(label='ChoiceField', choices=CHOICES)


class NewForm2(forms.Form):
    test1 = forms.BooleanField(label='BooleanField3.1')
    test2 = forms.BooleanField(label='BooleanField3.2')
    test3 = forms.BooleanField(label='BooleanField3.3')
