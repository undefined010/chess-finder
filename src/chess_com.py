import requests,json,datetime
from colorama import Fore as clr
import datetime


def get_req(url : str,err_msg : str):
    r = requests.get(url)

    if r.status_code != 200 :
        print (err_msg)
        return None
        
    return r.content

class GetChessInfo:
    URL = 'https://api.chess.com/pub/'
    
    @staticmethod
    def get_player_profile(username : str) -> dict:
        temp = dict()
        data = json.loads(get_req(GetChessInfo.URL + 'player/'+ username,'player may not found'))
        temp['last_online'] = datetime.datetime.utcfromtimestamp(int(data['last_online'])).strftime('%Y-%m-%d %H:%M:%S')
        temp['joined']      = datetime.datetime.utcfromtimestamp(int(data['joined'])).strftime('%Y-%m-%d %H:%M:%S')

        data.update(temp)
        return dict(data)
    
    @staticmethod
    def get_players_by_title(title : str) -> list:
        return list(json.loads(get_req(GetChessInfo.URL + 'titled/'+title,'title may not exist or an error occurred'))['players'])
    
    
    @staticmethod
    def get_players_by_country(iso : str) -> list:
        # max is 10000 from chess.com 
        return json.loads(get_req(f'https://api.chess.com/pub/country/{iso}/players','error'))['players']
    
    @staticmethod
    def get_clubs_by_country(iso) -> list:
        return json.loads(get_req(GetChessInfo.URL + f'country/{iso}/clubs','cheak the name'))['clubs']
        
    @staticmethod
    def get_country_name_chess_com_name(iso):
        return json.loads(get_req(GetChessInfo.URL + f'country/{iso}','error'))['name']
    
    @staticmethod
    def get_online_streamers() -> dict:
        
        data : list[dict] = json.loads(get_req(GetChessInfo.URL + 'streamers/','error'))['streamers']
        online_streamers : dict = dict()
        
        for streamer in data:
            if streamer['is_live']:
                online_streamers[streamer['username']] = streamer['twitch_url']
        
        return online_streamers

    @staticmethod   
    def save_output(fname : str, data : list) -> None:
        
        index : int = 0
        
        if data == None:
            print(clr.RED + 'No data')
            
        with open(f'output/{fname}.txt','a+') as af:
            
            af.write(f'time : {datetime.datetime.now} \n')
            for info in data:
                index += 1
                af.write(f'{index}) {str(info)} \n')
            af.close() 
