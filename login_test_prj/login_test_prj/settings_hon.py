from .settings_common import *

DEBUG = False
# mail（本番環境）
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp14.gmoserver.jp'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ning_wen@aliber.co.jp'
EMAIL_HOST_PASSWORD = 'czT$X7BD'
EMAIL_USE_TLS = False