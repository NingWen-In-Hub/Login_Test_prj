﻿from .settings_common import *

DEBUG = False
# mail（本番環境）
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jyrS$23Yta'
EMAIL_HOST_PASSWORD = 'Ning1488Google'
EMAIL_USE_TLS = False
