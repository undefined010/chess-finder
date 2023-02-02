import requests,json


class GetChessInfo:
    URL = 'https://api.chess.com/pub/'
    
    @staticmethod
    def get_player_profile(username : str) -> dict:
        r = requests.get(GetChessInfo.URL + 'player/'+ username)

        if r.status_code != 200 :
            print ('player may not exist or an error occurred')
            return None

        return json.loads(r.content)
    
    @staticmethod
    def get_players_by_title(title : str) -> list:
        r = requests.get(GetChessInfo.URL + 'titled/'+title)

        if r.status_code != 200 :
            print ('title may not exist or an error occurred')
            return None
        
        return json.loads(r.content)['players']

    @staticmethod
    def get_player_country(username : str) -> str:
        r = requests.get(GetChessInfo.URL + 'player/'+ username)

        if r.status_code != 200 :
            print ('player may not exist or an error occurred')
            return None
        
        return json.loads(r.content)['country']
        
    @staticmethod
    def get_online_streamers() -> None:
        r = requests.get(GetChessInfo.URL + 'streamers/')

        if r.status_code != 200 :
            print ('streamer may not exist or an error occurred')
            return None

        data : list[dict] = json.loads(r.content)['streamers']
        online_streamers : dict = dict()
        
        for streamer in data:
            if streamer['is_live']:
                online_streamers[streamer['username']] = streamer['twitch_url']

        return online_streamers
                
    
    
        
        