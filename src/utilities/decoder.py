from src.entities.team import Team
from src.entities.standing import Standing
from src.entities.table import Table
from src.entities.match import Match
from src.entities.league import League


def as_standings(obj):
    if 'currentround' in obj:
        return Table(*obj.values())
    if 'team' in obj:
        obj['team'] = Team(*obj['team'].values())
        return Standing(*obj.values())
    return obj


def as_matches(obj):
    if 'game_id' in obj:
        obj['league'] = League(*obj['league'].values())
        obj['home'] = Team(*obj['home'].values())
        obj['away'] = Team(*obj['away'].values())
        return Match(*obj.values())
    return obj
