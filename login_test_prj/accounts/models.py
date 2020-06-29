from django.db import models
from django.contrib.auth.models import AbstractUser

#AbstractUserを継承する
#DBのテーブルにアクセス用
class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta:
        verbose_name_plural = 'CustomUser'#モデルの名前
