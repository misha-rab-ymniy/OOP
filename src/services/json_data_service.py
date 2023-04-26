from src.services.idata_service import IDataService
from src.entities.table_container import TableContainer
from src.entities.match_container import MatchContainer
from src.utilities.encoder import EntitiesEncoder
import json


class JsonDataService(IDataService):
    @staticmethod
    def save_live_matches(match_container: MatchContainer):
        with open(f"../src/data/livematches.json", mode='w') as file:
            json.dump(match_container, file, cls=EntitiesEncoder, indent=2)

    @staticmethod
    def save_standings(table_container: TableContainer):
        with open(f"../src/data/standings/{table_container.season['league_id']}/"
                  f"{table_container.season['year'].replace('/', '_')}.json", mode='w') as file:
            json.dump(table_container, file, cls=EntitiesEncoder, indent=2)
