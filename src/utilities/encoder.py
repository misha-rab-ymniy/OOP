from src.entities.team import Team
from src.entities.standing import Standing
from src.entities.table import Table
from src.entities.table_container import TableContainer
from src.entities.league import League
from src.entities.match import Match
from src.entities.match_container import MatchContainer
import json


class EntitiesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, TableContainer):
            return obj.__dict__
        if isinstance(obj, Table):
            return obj.__dict__
        if isinstance(obj, Standing):
            return obj.__dict__
        if isinstance(obj, Team):
            return obj.__dict__
        if isinstance(obj, League):
            return obj.__dict__
        if isinstance(obj, MatchContainer):
            return obj.matches
        if isinstance(obj, Match):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
