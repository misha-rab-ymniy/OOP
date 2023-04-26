from src.services.item_factory import ItemFactory
from src.entities.table_container import TableContainer
from src.entities.match_container import MatchContainer
from src.utilities.decoder import as_matches, as_standings
from src.constants import TWO_YEAR_FORMAT
import json


class DataItemFactory(ItemFactory):
    @staticmethod
    def get_standings(league_id: int, season: str = None) -> TableContainer:
        if not season:
            season = '22_23' if league_id in TWO_YEAR_FORMAT else '2023'
        else:
            season.replace('/', '_')
        path = f"../src/data/standings/{league_id}/{season}.json"
        data = json.load(open(path), object_hook=as_standings)
        return TableContainer(**data)

    @staticmethod
    def get_live_matches(league_id: int = None):
        path = f"../src/data/livematches.json"
        data = json.load(open(path), object_hook=as_matches)
        match_container = MatchContainer(data)
        return match_container if not league_id else match_container.get_league_matches(league_id)
