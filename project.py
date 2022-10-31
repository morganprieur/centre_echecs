



from Controllers.player_controller import Player_controller 
from Models.player_model import Player 
from Views.dashboard_view import Dashboard_view 
from Views.get_player_view import Get_player_view 

# player test 
from test.player_test import Set_player_data 

import os

# TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
players_table = db.table('players') 

# # Dossier du projet 
# folder = os.path.dirname(__file__) 

# pour test 
from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 



if __name__ == "__main__": 

    # dashboard 
    # welcome = Dashboard_view.welcome_view(Dashboard_view) 
    
    # # Choix test ou pas : 
    # test_ou_pas = session.prompt('test ? (Y/N') 

    # if test_ou_pas == 'Y': 
    #     # test players 
    #     Set_player_data.test_players() 
    
    # else: 
    #     Get_player_view.prompt_for_player_data() 



    # # players 
    formated_players = Get_player_view.get_many_players() 
    players = Player_controller.instantiate_players(formated_players) 
    serialized_players = Player_controller.serialize_multi_players(players) 
    # print(f'serialized_players[0]["lastname"] ln51 : {serialized_players[0]["lastname"]}') 
    # print(f'serialized_players[1]["lastname"] ln51 : {serialized_players[1]["lastname"]}') 
    
    ### A mettre dans le model 
    # Vider la BDD avant d'enregistrer les nouveaux joueurs 
    # (ne pas le faire pour les tournois) 
    players_table.truncate() 
    # # Enregistrer les joueurs sérialisés dans la bdd : 
    players_table.insert_multiple(serialized_players) 






