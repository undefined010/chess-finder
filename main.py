from src.chess_com import GetChessInfo
import pyfiglet as pf
from colorama import Fore as clr

def show_options() -> None:
    options : list[str] = ['1) Get player profile','2) Get players by titled','3) Get online streamers']
    for option in options : print(clr.GREEN + option)

    
def save_data(data : dict) -> None:
    user: str = input(clr.BLUE + "Do you want to save data ?\n1)yes\n2)no\n=> ")
    
    if user.upper() == 'YES':
        fname : str = input(clr.GREEN + 'enter a name to txt file to save it or file path : ')
        GetChessInfo.save_output(fname,data)
        
    if user.upper() == 'NO':
        print(clr.BLUE + 'ok!')

def main() -> None:
    print(clr.RED + pf.figlet_format('Chess Finder'))
    print(clr.BLUE + 'press ctrl+c to exit...')

    while (True):
        try:
            show_options()
            option_input : str = input('-> ')

            if not option_input.isdigit():
                raise TypeError

            if int(option_input) == 1:
                chess_com_username : str = input(clr.RED + 'Enter a chess.com username : ')
                data : dict = GetChessInfo.get_player_profile(chess_com_username)
                for val,key in data.items(): print(clr.BLUE + '{} {}'.format(val,key))
                save_data(list(data.keys()) + list(data.values()))


            elif int(option_input) == 2:
                t : str = input(clr.GREEN + 'Enter a title in chess.com format ex Grand Master (GM): ')
                for data in GetChessInfo.get_players_by_title(t): print(clr.BLUE + data)
                save_data(GetChessInfo.get_players_by_title(t))
                
            elif int(option_input) == 3:
                data : dict = GetChessInfo.get_online_streamers()
                for val,key in data.items(): print(clr.BLUE + '{} {}'.format(val,key))
                save_data(list(data.values()))

        except KeyboardInterrupt:
            print (clr.RED + '\nGoodbye !',end='\n')
            break

    

if __name__ == '__main__':
    main()

