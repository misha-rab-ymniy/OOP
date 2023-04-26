from src.entities.match import Match


class MatchContainer:
    matches: list[Match]

    def __init__(self, matches: list[Match]):
        self.matches = matches

    def get_league_matches(self, league_id: int):
        return [match for match in self.matches if match.get_league_id() == league_id]

    def get_team_matches(self, team_id: int):
        return [match for match in self.matches if
                match.get_home_team_id() == team_id or match.get_away_team_id() == team_id][0]

    def __getitem__(self, val):
        return self.matches[val]

    def __str__(self):
        return str(self.matches)

    def __repr__(self):
        return str(self.matches)
