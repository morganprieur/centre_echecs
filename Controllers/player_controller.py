



from Models.player_model import Player 
from Views.get_player_data import Player_prompt_view 

import re 

# TinyDB 
from tinydb import TinyDB 

# TinyDB 
db = TinyDB('db.json') 
players_table = db.table('players') 



class Register_player(): 

    # Contrôleur : 


    # formated_players_data = Dashboard_view.formate_data(players_data=Dashboard_view.prompt_for_players_data()) 
    player_data = Player_prompt_view.prompt_for_player_data() 
    formated_player_data = Player_prompt_view.formate_data(player_data) 

    def instantiate_player(formated_player_data): 

        # Liste pour les joueurs objets 
        # players = [] 
        # pour débug 
        # count_players = 0 

        player = Player( 

            # for data_dict in range(len(formated_player_data)): 
            lastname=formated_player_data['lastname'], 
            firstname=formated_player_data['firstname'], 
            birthdate=formated_player_data['birthdate'], 
            genre=formated_player_data['genre'], 
            classement=formated_player_data['classement']
        ) 
            # print('player_x : ', player_x) 
            # players.append(player_x) 
        
        return player 


        # pour débug 
        # count_players += 1 if isinstance(player_x, player_model.Player) else count_players 
        # if count_players > 1: 
        #     print(f'There is {count_players} subscribers to the chess tournament') 
        # else: 
        #     print(f'There is {count_players} subscriber to the chess tournament') 

    # print('players : ', players) 
    # print('\n') 


    # # pour débug 
    # for pd in range(len(player_data)): 
    #     # print(f'pd : {pd}\n') 
    #     print(f'player_data[{pd}] : ', player_data[pd]) 
    #     print('\n') 

    player = instantiate_player(formated_player_data) 
    print(f'player in controller : {player}') 

    players = Player.list_players(player)  

    # Liste pour les joueurs sérialisés 
    serialized_players = Player.serialize_multi_players(players) 

    # Enregistrer les joueurs sérialisés dans la bdd : 
    players_table.truncate() 
    # players_table.insert(player1) # for 1 player 
    players_table.insert_multiple(serialized_players) 


