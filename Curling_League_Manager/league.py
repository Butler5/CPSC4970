from identified_object import IdentifiedObject


class League(IdentifiedObject):

    @property
    def teams(self):
        return self._teams

    @property
    def competitions(self):
        return self._competitions

    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._teams = []
        self._competitions = []

    def add_team(self, team):
        """SPEC: add team to the teams collection unless they are already in it (in which case do nothing)"""
        for i in self._teams:
            if prop.oid == i.oid:
                raise DuplicateOid("OID in use", team.oid)
        if team.oid not in [t.oid for t in self._teams]:
            self._teams.append(team)
        else:
            pass

    def remove_team(self, team):
        """SPEC: remove the team if they are in the teams list, otherwise do nothing"""
        for i in self._teams:
            self._teams.remove(team)
        else:
            pass

    def team_named(self, team_name):
        """SPEC: return the team in this league whose name equals team_name (case sensitive)
        or None if no such team exists"""
        for i in self._teams:
            if team_name == team_name:
                return team_name
            else:
                return None

    def add_competition(self, competition):
        """SPEC: add competition to the competitions collection"""
        for i in self.competitions:
            if prop.oid == i.oid:
                raise DuplicateOId("OID in use", competition.oid)
        self.competitions.append(competition)

    def teams_for_member(self, member):
        """SPEC: return a list of all teams for which member plays"""
        return [team for team in self._teams if member in team.members]

    def competitions_for_team(self, team):
        """SPEC: return a list of all competitions in which team is participating"""
        return [competition for competition in self._competitions if team in competition.teams_competing]

    def competitions_for_member(self, member):
        """SPEC: return a list of all competitions for which member played on one of the competing teams"""
        member_teams = [team for team in self._teams if member in team.members]
        return [competition for competition in self._competitions \
                if any(x in member_teams for x in competition.teams_competing)]

    def __str__(self):
        return f"{self.name}: {len(self._teams)} teams, {len(self._competitions)} competitions"
