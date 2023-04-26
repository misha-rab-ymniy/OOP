from src.constants import LEAGUES_ID
from datetime import datetime


class Formater:
    @staticmethod
    def live_matches(result: list):
        temp = result.copy()
        result.clear()
        result.extend(filter(lambda x: int(x['league']['id']) in LEAGUES_ID.values(), temp))
        for i, game in enumerate(result):
            result[i]['game_id'] = int(game['game_id'])
            result[i]['time'] = str(datetime.fromtimestamp(int(game['time'])))
            result[i]['league'] = {'id': int(game['league']['id']), 'name': game['league']['name'],
                                   'cc': game['league']['cc']}
            result[i]['home'] = {'id': int(game['home']['id']), 'name': game['home']['name'],
                                 'image_id': game['home']['image_id'], 'cc': game['home']['cc']}
            result[i]['away'] = {'id': int(game['away']['id']), 'name': game['away']['name'],
                                 'image_id': game['away']['image_id'], 'cc': game['away']['cc']}

    @staticmethod
    def league_table(result: dict, league_id: int):
        season_name = ""
        result["home"] = result["home"].pop("tables")
        result["away"] = result["away"].pop("tables")
        result["overall"] = result["overall"].pop("tables")
        for param in result["season"]:
            if param == "name":
                season_name = result["season"][param]
        result["season"].clear()
        if len(result["overall"]) == 1:
            result["season"]["type"] = "league"
        else:
            result["season"]["type"] = "cup"
        result["season"]["name"] = season_name[:-6]
        result["season"]["league_id"] = league_id
        result["season"]["year"] = season_name[-5:]

        for stands in result["home"]:
            for i, stand in enumerate(stands['rows']):
                Formater.__goal_diff(stand)
                stand['team']['id'] = int(stand['team']['id'])
                if not stand.get('promotion'):
                    Formater.__promotion(stand)

        for stands in result['away']:
            for i, stand in enumerate(stands['rows']):
                Formater.__goal_diff(stand)
                stand['team']['id'] = int(stand['team']['id'])
                if not stand.get('promotion'):
                    Formater.__promotion(stand)

        for stands in result['overall']:
            for i, stand in enumerate(stands['rows']):
                stand['team']['id'] = int(stand['team']['id'])
                if not stand.get('promotion'):
                    Formater.__promotion(stand)

        for stands in result['overall']:
            for stand in stands['rows']:
                stand['live_score'] = None

    @staticmethod
    def match(result: dict):
        res = result.copy()
        result.clear()
        result['match'] = {'game_id': int(res['id']), 'time': str(datetime.fromtimestamp(int(res['time']))),
                           'time_status:': res['time_status'],
                           'league': {'id': int(res['league']['id']), 'name': res['league']['name'],
                                      'cc': res['league']['cc']},
                           'home': {'id': int(res['home']['id']), 'name': res['home']['name'],
                                    'image_id': res['home']['image_id'], 'cc': res['home']['cc']},
                           'away': {'id': int(res['away']['id']), 'name': res['away']['name'],
                                    'image_id': res['away']['image_id'], 'cc': res['away']['cc']},
                           'timer': f"{res['extra']['length']}:00",
                           'score': res['ss'].replace('-', ':'),
                           'bey365_id': res['bet365_id']}
        result['scores'] = res['scores']
        result['stats'] = res['stats']
        result['extra'] = res['extra']
        result['events'] = res['events']

    @staticmethod
    def top_scorers(result):
        for param in result:
            for scorer in result[param]:
                scorer['player']['id'] = int(scorer['player']['id'])
                scorer['team']['id'] = int(scorer['team']['id'])

    @staticmethod
    def h2h(result):
        for key in result:
            for i, game in enumerate(result[key]):
                result[key][i] = {'game_id': int(game['id']), 'time': str(datetime.fromtimestamp(int(game['time']))),
                                  'time_status': game['time_status'], 'league': game['league'], 'home': game['home'],
                                  'away': game['away'], 'timer': None, 'score': game['ss'], 'bet365_id': None}
                result[key][i]['league']['id'] = int(game['league']['id'])
                result[key][i]['home']['id'] = int(game['home']['id'])
                result[key][i]['away']['id'] = int(game['away']['id'])

    @staticmethod
    def pre_match(result):
        temp = result.copy()
        result.clear()
        result.extend(filter(lambda x: int(x['league']['id']) in LEAGUES_ID.values(), temp))
        for game in result:
            game['time'] = str(datetime.fromtimestamp(int(game['time'])))
            game['game_id'] = int(game['game_id'])
            game['league'] = {'id': int(game['league']['id']), 'name': game['league']['name'],
                              'cc': game['league']['cc']}
            game['home'] = {'id': int(game['home']['id']), 'name': game['home']['name'],
                            'image_id': game['home']['image_id'], 'cc': game['home']['cc']}
            game['away'] = {'id': int(game['away']['id']), 'name': game['away']['name'],
                            'image_id': game['away']['image_id'], 'cc': game['away']['cc']}
            game['timer'] = None
            game['score'] = None
            game['bey365_id'] = None

    @staticmethod
    def __goal_diff(stand: dict):
        temp = dict((key, value) if key != 'extra' else (
            'goalDiffTotal', int(stand['goalsfor']) - int(stand['goalsagainst']))
                    for key, value in stand.items())
        stand.clear()
        for key, value in temp.items():
            stand[key] = value


    @staticmethod
    def __promotion(stand: dict):
        temp = stand.pop('team')
        stand['promotion'] = None
        stand['team'] = temp
        return stand
