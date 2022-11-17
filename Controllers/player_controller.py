



from Models.match_model import Match 
from Models.player_model import Player 
from Views.get_match_view import Get_match_view 
from Views.get_player_view import Get_player_view 

import re 

# TinyDB 
from tinydb import TinyDB, Query 
db = TinyDB('db.json') 
players_table = db.table('players') 


class Player_controller(): 


    def start(): 
        print('start for round 1') 

        # # players  --> à vérifier 
        # formated_players = Get_player_view.get_many_players() 
        # players = Player_controller.instantiate_players(formated_players) 
        # serialized_players = Player_controller.serialize_multi_players(players) 
        # print(f'serialized_players[0]["lastname"] ln51 : {serialized_players[0]["lastname"]}') 
        # print(f'serialized_players[1]["lastname"] ln51 : {serialized_players[1]["lastname"]}') 

    





