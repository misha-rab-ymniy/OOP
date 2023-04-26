import requests
from src.data_sources.formater import Formater
import json
from src.API_KEY import api_login, api_token

URL = f"https://spoyer.com/api/en/get.php?login={api_login}&token={api_token}&"


class Request:
    @staticmethod
    def get_league_table(league_id: int):
        request = requests.get(f'{URL}task=tabledata&league={league_id}')
        status_code = request.status_code
        if status_code == requests.codes.ok:
            result = request.json()['results']
            Formater.league_table(result, league_id)
            return result
        elif status_code == requests.codes.bad:
            raise APIErrorException('Invalid request. Check parameters.')
        elif status_code == requests.codes.forbidden:
            raise APIErrorException('This resource is restricted')
        elif status_code == requests.codes.not_found:
            raise APIErrorException('This resource does not exist. Check parameters')
        elif status_code == requests.codes.too_many_requests:
            raise APIErrorException('You have exceeded your allowed requests per minute/day')

    @staticmethod
    def get_live_matches(league_id: int = None):
        request = requests.get(f'{URL}task=livedata&sport=soccer')
        result = request.json()['games_live']
        Formater.live_matches(result)
        if league_id:
            return list(filter(lambda match: match['league']['id'] == league_id, result))
        else:
            return result

    @staticmethod
    def get_match(match_id: int):
        request = requests.get(f'{URL}task=eventdata&game_id={match_id}')
        result = request.json()['results'][0]
        Formater.match(result)
        return result

    @staticmethod
    def get_top_scorers(match_id: int):
        request = requests.get(f'{URL}task=leagueinfodata&league={match_id}')
        result = request.json()['results']
        Formater.top_scorers(result)
        return result

    @staticmethod
    def get_h2h_matches(match_id: int):
        request = requests.get(f'{URL}task=h2h&game_id={match_id}')
        result = request.json()['results']
        Formater.h2h(result)
        return result

    @staticmethod
    def get_pre_matches(day: str):
        request = requests.get(f'{URL}task=predata&sport=soccer&day=today')
        result = request.json()['games_pre']
        Formater.pre_match(result)
        return result


class APIErrorException(Exception):
    pass


# res = Request.get_league_table(123)
# with open("test.json", "w") as file:
#     json.dump(res, file, indent=2)
