



from Models.match_model import Match 
from Models.player_model import Player 
from Views.round_view import Round_view 
from Views.player_view import Player_view 

import re 

# TinyDB 
from tinydb import TinyDB, Query 
db = TinyDB('db.json') 
players_table = db.table('players') 


class Player_controller(): 

    # def __init__(self): 

    #     self.start() 

    ### possible ou pas ? comment faire ? ### 
    # players_to_register = int 
    # test_or_not = str 
    # formated_player_data = dict 
    # formated_player = list 

    # players = Player.players 

    def start(): 
        print('[Player_controller] start') 

        # # players  --> à vérifier ### 
        init_players = Player_view( 
            players_to_register=Player_view.players_to_register, 
            test_or_not=Player_view.test_or_not, 
            formated_player_data=Player_view.formated_player_data, 
            formated_players=Player_view.formated_players 
        ) 
        print(f'init_players C35 : {init_players}') 
        
        Player.instantiate_players(init_players.formated_players, Player.players) 
        # print(f'players PC53 : {Player.players}')  # ok 

        Player.serialize_multi_players(Player.players, Player.serialized_players) 
        # print(f'serialized_players PC57 : {Player.serialized_players}')     # ok 

        # print(f'serialized_players[0]["lastname"] ln51 : {serialized_players[0]["lastname"]}') 
        # print(f'serialized_players[1]["lastname"] ln51 : {serialized_players[1]["lastname"]}') 

    
