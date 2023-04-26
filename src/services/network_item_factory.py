from src.services.item_factory import ItemFactory
from src.entities.table_container import TableContainer
from src.data_sources.request import Request
from src.entities.match_container import MatchContainer
from src.utilities.decoder import as_standings, as_matches
from src.utilities.encoder import EntitiesEncoder
import json


class NetworkItemFactory(ItemFactory):
    @staticmethod
    def get_live_matches(league_id: int = None) -> MatchContainer:
        live_matches = json.dumps(Request.get_live_matches(league_id)).replace("'/g", '"')
        return MatchContainer(json.loads(live_matches, object_hook=as_matches))

    @staticmethod
    def get_standings(league_id: int, season: str = None) -> TableContainer:
        table = json.dumps(Request.get_league_table(league_id)).replace("/'/g", '"')
        return TableContainer(**json.loads(table, object_hook=as_standings))

    @staticmethod
    def get_pre_matches() -> MatchContainer:
        pre_matches = json.dumps(Request.get_pre_matches()).replace("'", '"')
        return MatchContainer(json.loads(pre_matches, object_hook=as_matches))
