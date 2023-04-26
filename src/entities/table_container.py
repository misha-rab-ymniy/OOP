from src.entities.table import Table


class TableContainer:
    season: dict
    overall: list[Table]
    home: list[Table]
    away: list[Table]

    def __init__(self, season, overall, home, away):
        self.season = season
        self.overall = overall
        self.home = home
        self.away = away

    def __str__(self):
        return f"{self.overall}, \n" \
               f"{self.home}, \n" \
               f"{self.away}"

    def get_league_id(self):
        return self.season["league_id"]

    def get_overall_table(self):
        if self.season['type'] == 'league':
            return self.overall[0]
        else:
            return self.overall

    def get_home_table(self):
        if self.season['type'] == 'league':
            return self.home[0]
        else:
            return self.home

    def get_away_table(self):
        if self.season['type'] == 'league':
            return self.away[0]
        else:
            return self.away

    def make_live_standing(self, home_team_id: int, away_team_id: int, live_score: str):
        if self.season['type'] == 'league':
            self.overall[0].make_live_standings(home_team_id, away_team_id, live_score)
        else:
            for table in self.overall:
                table.make_live_standings(home_team_id, away_team_id, live_score)

    def update(self, *args):
        self.season = args[0]
        self.overall = args[1]
        self.home = args[2]
        self.away = args[3]
