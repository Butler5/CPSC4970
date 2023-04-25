import csv
import os.path


class LeagueDatabase:

    _sole_instance = None

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def load(cls, file_name):
        """loads a LeagueDatabase from the specified file and stores it in _sole_instance"""
        try:
            with open(file_name, mode="rb") as f:
                cls._sole_instance = pickle.load(f)
        except FileExistsError:
            print("File does not exist")
        except:
            try:
                with open(file_name+".backup", mode="rb") as f:
                    cls._sole_instance = pickle.load(f)
            except FileExistsError:
                print("Backup file does not exist")

    def __init__(self):
        self._last_oid = 0
        self.leagues = []

    @property
    def last_oid(self):
        return self._last_oid

    def add_league(self, league):
        """add the specified league to the leagues list"""
        self.leagues.append(league)

    def remove_league(self, league):
        """remove the specified league from the leagues list"""
        if league in self.leagues:
            self.leagues.remove(league)

    def league_name(self, name):
        """return the league with the given name or None of no such league exists"""
        if league in self.leagues:
            return league

    def next_oid(self):
        """increment _last_id and return its new value"""
        self._last_oid = self._last_oid + 1
        return self._last_oid

    def save(self, file_name):
        """save this database on the specified file"""
        if os.path.exists(file_name):
            file_name = file_name + ".backup"
        with open(file_name, mode="wb") as f:
            pickle.dump(self._sole_instance, f)

    def import_league_teams(self, league, file_name):
        """load the teams and team members in a league from a CSV formatted file"""
        league = League(self.instance().next_oid(), league_name)
        team_name = ""
        try:
            with open(file_name, 'r', encoding="utf-8", newline="\n") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if team_name != "":
                        league.add_team(team)
                    team_name = row["Team name"]
                    team = Team(self.instance().next_oid(), row["Team name"])
                member = TeamMember(self.instance().next_oid(), row["Member name"], row["Member email"])
                team.add_member(member)
            league.add_team(team)
            self.instance().add_league(league)
        except:
            print("An error occurred importing league info")

    def export_league_teams(self, league, file_name):
        """write the specified league to a CSV formatted file"""
        if league not in self.leagues:
            print("An error occurred exporting league info")
        else:
            try:
                with open(file_name, 'w', encoding="utf-8", newline="\n") as csvfile:
                    fieldnames = ['Team name', 'Member name', 'Member email']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for team in league.teams:
                        for member in team.add_members:
                            writer.writerow({'Team name': team.name, 'Member name': member.name,
                                           + 'Member email': member.email})
            except:
                print("An error occurred exporting league info")

