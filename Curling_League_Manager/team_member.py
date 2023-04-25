from identified_object import IdentifiedObject


class TeamMember(IdentifiedObject):

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def __init__(self, oid, name, email):
        super().__init__(oid)
        self._name = name
        self._email = email

    def send_email(self, emailer, subject, message):
        """SPEC: send an email to to this member"""
        emailer.send_plain_email([self.email], subject, message)

    def __str__(self):
        return f"{self.name}<{self.email}>"
