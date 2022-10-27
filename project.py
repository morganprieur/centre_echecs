



# from Views.dashboard_view import Dashboard_view 
# from Controllers.players_controller import Register_players  
# from Models.player_model import Player 

import os

from Controllers import player_controller 
# Dossier du projet 
folder = os.path.dirname(__file__) 
# functions 
# from utils.functions import prompt_for_players_data, serialize_multi_players, try_modules 
# from Controllers.players_controller import Register_players 

# TinyDB 
from tinydb import TinyDB 

# TinyDB 
db = TinyDB('db.json') 
players_table = db.table('players') 


# from . import Classe2
# #ou
# from .Classes import Classe2


# class Trying(): 

#     # pl = Player(firstname='firstname', lastname='lastname', birthdate='2022-10-13', genre='M', classement='45') 
#     # print(pl) 

#     print('trying class') 

#     ojd = try_modules('pluie') 


if __name__ == "__main__": 
#     from utils.functions import prompt_for_players_data, serialize_multi_players 
    from Models.player_model import Player 
    from Controllers.player_controller import Register_player 
    from Views.get_player_data import Player_prompt_view 


    formated_players = Player_prompt_view.get_many_players() 
    players = Register_player.instantiate_players(formated_players) 
    serialized_players = Register_player.serialize_multi_players(players) 
    # print(f'serialized_players[0]["lastname"] ln51 : {serialized_players[0]["lastname"]}') 
    # print(f'serialized_players[1]["lastname"] ln51 : {serialized_players[1]["lastname"]}') 
    
    players_table.truncate() 
    # # Enregistrer les joueurs sérialisés dans la bdd : 
    players_table.insert_multiple(serialized_players) 






