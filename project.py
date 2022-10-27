



import os

from Controllers import player_controller 

# TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
players_table = db.table('players') 

# # Dossier du projet 
# folder = os.path.dirname(__file__) 



if __name__ == "__main__": 

    from Models.player_model import Player 
    from Controllers.player_controller import Register_player 
    from Views.get_player_data import Player_prompt_view 


    formated_players = Player_prompt_view.get_many_players() 
    players = Register_player.instantiate_players(formated_players) 
    serialized_players = Register_player.serialize_multi_players(players) 
    # print(f'serialized_players[0]["lastname"] ln51 : {serialized_players[0]["lastname"]}') 
    # print(f'serialized_players[1]["lastname"] ln51 : {serialized_players[1]["lastname"]}') 
    
    # Vider la BDD avant d'enregistrer les nouveaux joueurs 
    # (ne pas le faire pour les tournois) 
    players_table.truncate() 
    # # Enregistrer les joueurs sérialisés dans la bdd : 
    players_table.insert_multiple(serialized_players) 






