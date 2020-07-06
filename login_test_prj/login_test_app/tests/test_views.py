from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Profile, UserSpecies
import logging

logger = logging.getLogger(__name__)


class LogInTestCase(TestCase):
    """各テストクラスで共通の事前準備処理"""

    def setUp(self):
        """テストメソッド実行前の事前設定"""
        self.password = 'AAAA123456'
        self.test_user = get_user_model().objects.create_user(
            username='ww1',
            email='ww1@ww.com',
            password=self.password
        )

        self.client.login(email=self.test_user.email,
                          password=self.password)


class TestProfileCreateView(LogInTestCase):
    """ProfileCreateViewのテストクラス"""
    logger.debug("ProfileCreateViewのテストクラス")

    def test_create_profile_success(self):
        """作成成功を検証"""
        # test用species
        UserSpecies.objects.create(id='0', species='分からない')
        # 実行する前、DBにはデータがないこと
        self.assertEqual(Profile.objects.all().count(), 0)
        # Postパラメータ
        params = {'age': '862',
                  'names': '名前',
                  'photo': '',
                  'species': '0',
                  }
        # Post実行（self.client）
        response = self.client.post(reverse_lazy('login_test_app:profile_create'), params)

        # 検証（self.assert）
        self.assertRedirects(response, reverse_lazy('login_test_app:profile'))
        self.assertEqual(Profile.objects.all().count(), 1)
        # self.assertEqual(Profile.objects.get(pk=1).names, '名前')
        # self.assertEqual(Profile.objects.get(pk=1).species,
        # UserSpecies.objects.get(species='分からない'))
        self.assertEqual(Profile.objects.get(names='名前').species,
                         UserSpecies.objects.get(species='分からない'))

    def test_create_profile_failure(self):
        """作成失敗を検証"""
        response = self.client.post(reverse_lazy('login_test_app:profile_create'))

        # 必須チェック
        self.assertFormError(response, 'form', 'names', 'このフィールドは必須です。')

    class TestProfileEdit(LogInTestCase):
        """ProfileEditのテストクラス"""
        logger.debug("ProfileEditViewのテストクラス")

        def test_profile_edit_success(self):
            """編集処理成功"""

            profile = Profile.objects.create(user=self.test_user, names='編集前名前')

            params = {'names': '編集後名前'}
            response = self.client.post(reverse_lazy('login_test_app:profile_edit',
                                                     kwargs={'pk': profile.pk}), params)
            self.assertRedirects(response, reverse_lazy('login_test_app:profile'))
            self.assertEqual(response.objects.get(pk=profile.pk).names, '編集後名前')

        def test_profile_edit_failure(self):
            response = self.client.post(reverse_lazy('login_test_app:profile_edit',
                                                     kwargs={'pk': 999}))
            self.assertEqual(response.status_code, 404)  # 403を追
