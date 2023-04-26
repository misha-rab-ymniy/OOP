from src.entities.standing import Standing


class Table:
    name: str
    group_name: str
    currentround: str
    max_rounds: str
    standings: list[Standing]

    def __init__(self, name: str, group_name: str, current_round: str, max_rounds: str, standings: list):
        self.name = name
        self.group_name = group_name
        self.currentround = current_round
        self.max_rounds = max_rounds
        self.standings = standings

    def __str__(self):
        return f"Table (name: {self.name}, group_name: {self.group_name}, current_round: {self.currentround}, " \
               f"max_rounds: {self.max_rounds}, standings: {self.standings})"

    def __repr__(self):
        return f"Table (name: {self.name}, group_name: {self.group_name}, current_round: {self.currentround}, " \
               f"max_rounds: {self.max_rounds}, standings: {self.standings})"

    def get_standings(self):
        return self.standings

    def sort_standings(self):
        self.standings.sort(key=lambda s: s.get_points(), reverse=True)

    @staticmethod
    def __to_result_format(res):
        if res[0] > res[-1]:
            return 'w'
        if res[0] < res[-1]:
            return 'l'
        return 'd'

    def make_live_standings(self, home_team_id: int, away_team_id: int, live_score: str):
        res = self.__to_result_format(live_score)

        if res == 'w':
            for stand in self.standings:
                if stand.get_team_id() == home_team_id:
                    stand.add_points(3)
                    stand.set_live_score(live_score)
                if stand.get_team_id() == away_team_id:
                    stand.set_live_score(live_score[::-1])
        elif res == 'l':
            for stand in self.standings:
                if stand.get_team_id() == away_team_id:
                    stand.add_points(3)
                    stand.set_live_score(live_score[::-1])
                if stand.get_team_id() == home_team_id:
                    stand.set_live_score(live_score)
        else:
            for stand in self.standings:
                if stand.get_team_id() == home_team_id or stand.get_team_id() == away_team_id:
                    stand.add_points(1)
                    stand.set_live_score(live_score)
                    stand.set_live_score(live_score)

        self.sort_standings()

        for i, stand in enumerate(self.standings):
            stand.make_right_pos(i + 1)
