from src.services.network_item_factory import NetworkItemFactory
from src.services.json_data_service import JsonDataService
from src.constants import LEAGUES_ID


class Updater:
    @staticmethod
    def live_results():
        print("Updater live results")
        live_matches = NetworkItemFactory.get_live_matches()
        JsonDataService.save_live_matches(live_matches)
        for match in live_matches:
            if match.get_time_status() == '3':
                JsonDataService.save_standings(NetworkItemFactory.get_standings(match.get_league_id()))

    @staticmethod
    def all():
        JsonDataService.save_live_matches(NetworkItemFactory.get_live_matches())
        for league_name in LEAGUES_ID:
            JsonDataService.save_standings(NetworkItemFactory.get_standings(LEAGUES_ID[league_name]))
