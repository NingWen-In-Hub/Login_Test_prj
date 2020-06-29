import logging
from django.core.exceptions import (
    ValidationError,
)

logger = logging.getLogger(__name__)


class MyPasswordValidator:
    """
    最初値は0ではない検証
    """

    def __init__(self, ban_word='0'):  # initial イニシャル
        self.ban_word = ban_word

    def validate(self, password, user=None):
        logger.info("ban word:{};password:{}".format(self.ban_word, password[0]))
        if password[0] == self.ban_word:
            # if password.find(self.ban_word) != -1: # 0を入らないように
            raise ValidationError(
                ("パスワードは「{}」で始まるのはいけません。".format(self.ban_word)),
                code='password_my_ban',
            )

    def get_help_text(self):
        return "パスワードは「{}」で始まるのはいけません。".format(self.ban_word)
