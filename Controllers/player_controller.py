



from Models.match_model import Match 
from Models.player_model import Player 
from Views.match_view import Match_view 
from Views.player_view import Player_view 

import re 

# TinyDB 
from tinydb import TinyDB, Query 
db = TinyDB('db.json') 
players_table = db.table('players') 


class Player_controller(): 

    # def __init__(self): 

    #     self.start() 


    def start(): 
        print('[Player_controller] start for round 1') 

        # # players  --> à vérifier 
        init_players = Player_view( 
            players_to_register=Player_view.players_to_register, 
            test_or_not=Player_view.test_or_not, 
            formated_player_data=Player_view.formated_player_data, 
            formated_players=Player_view.formated_players 
        ) 
        print(f'init_players C35 : {init_players}') 
        print(f'init_players.formated_players C36 : {init_players.formated_players}') 
        print(f'init_players.formated_players C37 : {init_players.players_to_register}') 
        print(f'init_players.formated_players C38 : {init_players.test_or_not}') 

        # formated_players = Player_view.get_players(init_players) 
        # print(f'formated_players C40 : {formated_players}') 

        players = Player.instantiate_players(init_players.formated_players) 
        # print(f'players C41 : {players}')   # ok 

        serialized_players = Player.serialize_multi_players(players) 
        # print(f'serialized_players C44 : {serialized_players}')     # ok 

        # print(f'serialized_players[0]["lastname"] ln51 : {serialized_players[0]["lastname"]}') 
        # print(f'serialized_players[1]["lastname"] ln51 : {serialized_players[1]["lastname"]}') 

    





