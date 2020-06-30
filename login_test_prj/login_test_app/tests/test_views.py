from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Profile


class LogInTestCase(TestCase):
    """各テストクラスで共通の事前準備処理"""
    def setUp(self):
        """テストメソッド実行前の事前設定"""
        self.password = 'AAAA123456'
        self.test_user = get_user_model().objects.create_user(
            username='blackcat',
            email='blackcat@white.com',
            password=self.password
        )

        self.client.login(email=self.test_user.email,
                          password=self.password)


class TestProfileCreateView(LogInTestCase):
    """ProfileCreateViewのテストクラス"""
    def test_create_profile_success(self):
        # Postパラメータ
        params = {'names': '名前',
                  'age': '862',
                  'photo': ''
                  }
        # Post実行（self.client.post）
        response = self.client.post(reverse_lazy('login_test_app:profile_create'), params)
        # 検証（self.assert）
        self.assertRedirects(response, reverse_lazy('login_test_app:profile_create'))
        self.assertEqual(Profile.objects.fliter(names='名前').count(), 1)

    def test_create_profile_failure(self):
        """作成失敗を検証"""
        response = self.client.post(reverse_lazy('login_test_app:profile_create'))

        # 必須チェック
        self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。')

    class TestProfileEdit(LogInTestCase):
        """ProfileEditのテストクラス"""

        def test_profile_edit_success(self):
            """編集処理成功"""

            profile = Profile.objects.creat(user=self.test_user, names='編集前名前')
            params = {'names': '編集後名前'}

            response = self.client.post(reverse_lazy('login_test_app:profile_edit',
                                                     kwargs={'pk': profile.pk}), params)
            self.assertRedirects(response, reverse_lazy('login_test_app:profile'))
            self.assertEqual(response.objects.get(pk=profile.pk).names, '編集後名前')

        def test_profile_edit_failure(self):
            response = self.client.post(reverse_lazy('login_test_app:profile_edit',
                                                     kwargs={'pk': 999}))
            self.assertEqual(response.status_code, 403)
