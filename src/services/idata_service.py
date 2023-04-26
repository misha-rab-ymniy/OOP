from abc import ABC, abstractmethod
from src.entities.match_container import MatchContainer
from src.entities.table_container import TableContainer


class IDataService(ABC):
    @staticmethod
    @abstractmethod
    def save_live_matches(match_container: MatchContainer):
        """Сохранить лaйф игры"""

    @staticmethod
    @abstractmethod
    def save_standings(table_container: TableContainer):
        """Сохранить положение команд"""
