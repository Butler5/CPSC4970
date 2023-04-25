from identified_object import IdentifiedObject


class Team(IdentifiedObject):

    @property
    def members(self):
        return self._team_members

    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._team_members = []

    def add_member(self, member):
        """SPEC: ignore request to add team member that is already in members"""
        members_emails = []
        for i in self.members:
            members_emails.append(i.email)
        if member not in self.members:
            self._team_members.append(member)

    def member_named(self, s):
        """SPEC: return the member of this team whose name equals s
                (case sensitive) or None if no such member exists"""
        for s in self.members:
            return self.name
        else:
            return None

    def remove_member(self, member):
        """SPEC: remove the specified member from this team"""
        if member in self._team_members:
            self._team_members.remove(member)

    def send_email(self, emailer, subject, message):
        """SPEC:  send an email to all members of a team except those whose email address is None."""
        members_emails = []
        subject = "Test"
        message = "Hello, world!"
        for x in self.members:
            members_emails.append(x.email)
        emailer.send_plain_email(members_emails, subject, message)

    def __str__(self):
        return f"{self.name}: {len(self.members)} members"
