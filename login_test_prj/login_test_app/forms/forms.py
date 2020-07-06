from django import forms
from django.forms import ModelForm
from django.core.mail import EmailMessage
from login_test_app.models import Profile, UserSpecies
from .forms2 import AddForm2
from django.forms import MultiWidget
import logging

logger = logging.getLogger(__name__)


class InquiryForm(forms.Form):
    # テキストボックス　と　フォームバリデーション（入力チェック）
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # col-widget
        self.fields['name'].widget.attrs['class'] = 'form-control col-15'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力してください'

        self.fields['email'].widget.attrs['class'] = 'form-control col-15'

        self.fields['message'].widget.attrs['class'] = 'form-control col-15'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ　メール送信'  # メールのタイトル
        message = '送信者名： {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, message)
        from_email = 'admin@toppage.com'
        to_list = [
            'admin@toppage.com'
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()


# class AddForm(InquiryForm):
class AddForm(AddForm2):  # 他のformsからの継承
    test1 = forms.BooleanField(label='BooleanField')
    CHOICES = (('1', 'ラーメン'), ('2', 'ソウメン'), ('3', 'イケメン'))
    test2 = forms.ChoiceField(label='ChoiceField', choices=CHOICES)
    test3 = forms.TypedChoiceField(label='TypedChoiceField', coerce='int')
    # 強制的指定した型にすることができる
    test3.choices = CHOICES + (('5', 'バナナ'),)
    # 後でパラメータを追加
    test4 = forms.URLField(label='URLField')
    test5 = forms.MultipleChoiceField(label='MultipleChoiceField', choices=CHOICES)
    test6 = forms.NullBooleanField(label='NullBooleanField')
    test7 = forms.MultipleChoiceField(label='MultipleChoiceField', choices=CHOICES,
                                      widget=forms.RadioSelect(attrs={
                                          'id': 't-2048', 'class': 'form-check-input'}))


class ProfileEditForm(forms.ModelForm):
    """プロフィール作成、編集form"""
    CHOICES = UserSpecies.objects.filter(id__lt='5')
    logger.info("種族ID＜5：{}".format(CHOICES))
    """test2 = forms.ModelChoiceField(label='ChoiceField', queryset=CHOICES)
    test3 = forms.ModelMultipleChoiceField(label='CheckboxField', queryset=CHOICES,
                                           widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}))
    test4 = forms.ModelMultipleChoiceField(label='radio', queryset=CHOICES,
                                           widget=forms.RadioSelect(attrs={'class': 'radio'}))
"""
    class Meta:
        model = Profile
        # exclude = ()  # created_at,updated_atは編集できないfields
        exclude = ("user", "created_at", "updated_at")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
