from src.entities.league import League
from src.entities.team import Team


class Match:
    game_id: str
    time: str
    time_status: str
    league: League
    home: Team
    away: Team
    timer: str
    score: str
    bet365_id: str

    def __init__(self, game_id: str, time: str, time_status: str, league: League, home: Team, away: Team, timer: str,
                 score: str, bet365_id: str):
        self.game_id = game_id
        self.time = time
        self.time_status = time_status
        self.league = league
        self.home = home
        self.away = away
        self.timer = timer
        self.score = score
        self.bet365_id = bet365_id

    def __repr__(self):
        return f"Match (game_id: {self.game_id}, time: {self.time}, time_status: {self.time_status}, " \
               f"league: {self.league})"

    def __str__(self):
        return f"Match (game_id: {self.game_id}, time: {self.time}, time_status: {self.time_status}, " \
               f"league: {self.league})"

    def get_league_id(self):
        return self.league.get_id()

    def get_home_team_id(self):
        return self.home.get_id()

    def get_away_team_id(self):
        return self.away.get_id()

    def get_score(self):
        return self.score

    def get_time_status(self):
        return self.time_status
