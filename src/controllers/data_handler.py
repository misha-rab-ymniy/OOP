from src.controllers.data_updater import Updater
from src.services.data_item_factory import DataItemFactory
import time
import asyncio
import schedule


class DataHandler:
    def __init__(self):
        pass
        # Updater.all()

    @staticmethod
    def get_standings(league_id: int):
        table = DataItemFactory.get_standings(league_id)
        live_matches = DataItemFactory.get_live_matches(league_id)
        for match in live_matches:
            if match.get_time_status() == '1':
                table.make_live_standing(match.get_home_team_id(), match.get_away_team_id(), match.get_score())
        return table

    @staticmethod
    def get_live_matches(league_id: int = None):
        return DataItemFactory.get_live_matches(league_id)
