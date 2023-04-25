from team import Team
import yagmail


class Emailer:
    """SINGLETON"""
    sender_address = ""
    _sole_instance = None

    @classmethod
    def configure(cls, sender_address):
        cls.sender_address = sender_address

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    def send_plain_email(self, recipients, subject, message):

        for i in self._recipients:
            print(f"Sending mail to:{recipients}")