import requests,json,datetime

"""
    converty time stamps into readable time format
"""

def get_req(url,err_msg):
    r = requests.get(url)

    if r.status_code != 200 :
        print (msg)
        return None
        
    return r.content

class GetChessInfo:
    URL = 'https://api.chess.com/pub/'
    
    @staticmethod
    def get_player_profile(username : str) -> dict:
        return json.loads(get_req(GetChessInfo.URL + 'player/'+ username,'player may not found'))
    
    @staticmethod
    def get_players_by_title(title : str) -> list:
        return json.loads(get_req(GetChessInfo.URL + 'titled/'+title,'title may not exist or an error occurred'))['players']
    
    
    @staticmethod
    def get_players_by_country(iso : str) -> list:
        # max is 10000 from chess.com 
        return json.loads(get_req(GetChessInfo.URL + 'country/{iso}/players','cheak the name'))['players']
    
    
    @staticmethod
    def get_clubs_by_country() -> list:
        return json.loads(get_req(GetChessInfo.URL + 'country/clubs','cheak the name'))['clubs']
        
    @staticmethod
    def get_country_chess_com_name() -> str:
        return json.loads(get_req(GetChessInfo.URL + 'country/','error'))['name']
    
    @staticmethod
    def get_online_streamers() -> None:
        
        data : list[dict] = json.loads(get_req(GetChessInfo.URL + 'streamers/','error'))['streamers']
        online_streamers : dict = dict()
        
        for streamer in data:
            if streamer['is_live']:
                online_streamers[streamer['username']] = streamer['twitch_url']
        
        return online_streamers
        
    @staticmethod
    def save_output(fname : str, data : dict) -> None:
        if data == None:
            print(clr.RED + 'No data')
            
        with open(f'{fname}.txt','a+') as af:
            for val , key in data.items():
                af.write(f'{str(key)} : {str(val)} \n')
                af.close()
    
    @staticmethod   
    def save_output(fname : str, data : list) -> None:
        
        index : int = 0
        
        if data == None:
            print(clr.RED + 'No data')
            
        with open(f'{fname}.txt','a+') as af:
            counter += 1
            af.write(f'time : {datetime.datetime.now} \n')
            for info in data:
                af.write(f'{index}) {str(info)} \n')
                af.close()
                
    
    
        
        