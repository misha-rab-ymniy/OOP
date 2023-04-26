from abc import ABC, abstractmethod


class ItemFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_standings(league_id: int, season: str = None):
        """ Get a table of league """

    @staticmethod
    @abstractmethod
    def get_live_matches(league_id: int = None):
        """ Get live matches """
