



from Controllers.player_controller import Player_controller 
from Controllers.match_controller import Match_controller 
# from Models.player_model import Player 
# from Models.match_model import Match 
# from Views.dashboard_view import Dashboard_view 
# from Views.get_player_view import Get_player_view 

# player test 
# from test.player_test import Get_player_data 

import os

# # Dossier du projet 
# folder = os.path.dirname(__file__) 

from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 



if __name__ == "__main__": 

    Player_controller.start() 
    
    # matches 
    # Match_controller.insantiate_match() 

    # # dashboard 
    # # welcome = Dashboard_view.welcome_view(Dashboard_view) 


    # # players     --> à corriger (répartition : contrôle des données dans le conrôleur !) 
    # formated_players = Get_player_view.get_many_players() 
    # players = Player_controller.instantiate_players(formated_players) 
    # serialized_players = Player_controller.serialize_multi_players(players) 
    # # print(f'serialized_players[0]["lastname"] ln51 : {serialized_players[0]["lastname"]}') 
    # # print(f'serialized_players[1]["lastname"] ln51 : {serialized_players[1]["lastname"]}') 
    
    # project : 
    #   while players_to_register > 0: 
    #       Vue : prompt_for_players_data 
    #       Controleur : formate_data (+ groupe dans une lsite de dicts) 
    #   Modèle : instantiate_players 
    #   Modèle : serialize_players 
    #   Modèle : insert_multiple 

    # # Vider la BDD avant d'enregistrer les nouveaux joueurs 
    # # (ne pas le faire pour les tournois, si on doit garder un historique des tournois) 
    # players_table.truncate() 
    # # # Enregistrer les joueurs sérialisés dans la bdd : 
    # players_table.insert_multiple(serialized_players) 



