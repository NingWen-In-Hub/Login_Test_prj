from accounts.models import CustomUser
from django.db import models


class UserSpecies(models.Model):
    """ユーザー種族モジュール"""
    id = models.SmallIntegerField(primary_key=True, verbose_name='id')
    species = models.CharField(verbose_name='種族', max_length=5, blank=True, null=True)

    class Mata:
        verbose_name_plural = 'UserSpecies'

    def __str__(self):
        return self.species


class Profile(models.Model):
    """個人情報モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT, related_name='p_names')
    # on_delete: models.CASCADE(一緒に削除);models.PROTECT(保留);models.SET_NULL(nullにする);
    #            models.SET_DEFAULT(defaultにする);models.SET()(値にする);DO_NOTHING;
    names = models.CharField(verbose_name='お名前', max_length=20)
    age = models.SmallIntegerField(verbose_name='年齢', null=True)
    # species = models.CharField(verbose_name='種族', max_length=5, blank=True, null=True)
    species = models.ForeignKey(UserSpecies, verbose_name='種族', on_delete=models.SET(0), related_name='p_species')
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Mata:
        verbose_name_plural = 'Profile'

    # 　文字列でクラスを表示する
    def __str__(self):
        return self.names


