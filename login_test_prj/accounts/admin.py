from django.contrib import admin
from .models import CustomUser

#モデルを管理サイトに新しく表示させる
admin.site.register(CustomUser)
