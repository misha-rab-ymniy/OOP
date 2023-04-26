from src.entities.team import Team


class Standing:
    pos: str
    sort_pos: str
    change: str
    win: str
    draw: str
    loss: str
    goals_for: str
    goals_against: str
    points: str
    pct: str
    goal_diff_total: int
    promotion: dict
    team: Team
    live_score: str
    live_res: str

    def __init__(self, pos: str, sort_pos: str, change: str, win: str, draw: str, loss: str, goals_for: str,
                 goals_against: str, points: str, pct: str, goal_diff_total: int, promotion: dict, team: Team,
                 live_score: str = None, live_res: str = None):
        self.pos = pos
        self.sort_pos = sort_pos
        self.change = change
        self.win = win
        self.draw = draw
        self.loss = loss
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.points = points
        self.pct = pct
        self.goal_diff_total = goal_diff_total
        self.promotion = promotion
        self.team = team
        self.live_score = live_score
        self.live_res = live_res

    def __repr__(self):
        return f"Standing (pos: {self.pos}, sort_pos: {self.sort_pos}, change: {self.change}, win: {self.win}, " \
               f"draw: {self.draw}, loss: {self.loss}, goals_for: {self.goals_for}, goals_against: {self.goals_against}," \
               f" points: {self.points}, pct: {self.pct}, goal_diff_total: {self.goal_diff_total}, promotion: " \
               f"{self.promotion}, team: {self.team}, live_score: {self.live_score})"

    def __str__(self):
        return f"Standing (pos: {self.pos}, sort_pos: {self.sort_pos}, change: {self.change}, win: {self.win}, " \
               f"draw: {self.draw}, loss: {self.loss}, goals_for: {self.goals_for}, goals_against: {self.goals_against}," \
               f" points: {self.points}, pct: {self.pct}, goal_diff_total: {self.goal_diff_total}, promotion: " \
               f"{self.promotion}, team: {self.team}, live_score: {self.live_score})"

    def set_live_score(self, live_score: str):
        self.live_score = live_score

    def get_points(self):
        return self.points

    def get_pos(self):
        return self.pos

    def get_team_id(self):
        return self.team.id

    def make_right_pos(self, position: int):
        self.change = str(int(self.pos) - position + int(self.change))
        self.pos = str(position)

    def add_points(self, num_points: int):
        self.points = str(int(self.points) + num_points)
