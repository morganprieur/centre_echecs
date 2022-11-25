



from Controllers.match_controller import Match_controller 
from Controllers.player_controller import Player_controller 
from Controllers.round_controller import Round_controller 
from Models.match_model import Match 
from Models.player_model import Player 
from Views.dashboard_view import Dashboard_view 
# from Views.get_player_view import Get_player_view 
# from Views.match_view import Match_view 

# player test 
# from test.player_test import Get_player_data 

import os

# # TinyDB 
# from tinydb import TinyDB 
# db = TinyDB('db.json') 
# players_table = db.table('players') 

# # Dossier du projet 
# folder = os.path.dirname(__file__) 
 
# from prompt_toolkit import PromptSession 
# # to use prompt as an instance 
# session = PromptSession() 



if __name__ == "__main__": 

    Player_controller.start() 

    # player_x = Player( 
    #     lastname=formated_players[data_dict]['lastname'], 
    #     firstname=formated_players[data_dict]['firstname'], 
    #     birthdate=formated_players[data_dict]['birthdate'], 
    #     genre=formated_players[data_dict]['genre'], 
    #     classement=formated_players[data_dict]['classement']
    # )  

    # dashboard 
    # welcome = Dashboard_view.welcome_view(Dashboard_view) 
    
    # Player_controller.start() 
    Match_controller.start_matches() 
    Round_controller.start_round_1() 
    
    # p_table_class = Player_controller.sort_players_by_classement()  # Player 
    # players_ids = Player_controller.get_players_ids(p_table_class) 

    
    



    ### A mettre dans le model 
    # Vider la BDD avant d'enregistrer les nouveaux joueurs 
    # (ne pas le faire pour les tournois, si on doit garder un historique des tournois) 
    # players_table.truncate() 
    # # # Enregistrer les joueurs sérialisés dans la bdd : 
    # players_table.insert_multiple(serialized_players) 

