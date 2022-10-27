



from Models.player_model import Player 
# from Views.get_player_data import Player_prompt_view 

import re 

# TinyDB 
from tinydb import TinyDB 

# TinyDB 
db = TinyDB('db.json') 
players_table = db.table('players') 



class Register_player(): 

    # Contrôleur : 

    # formated_players = Player_prompt_view.get_many_players() 

    # def instantiate_players(formated_players=Player_prompt_view.get_many_players): 
    def instantiate_players(formated_players): 

        # print(f'formated_player_data cont_ln32 : {formated_player_data}') 

        # Liste pour les joueurs objets 
        players = [] 
        # pour débug 
        # count_players = 0 

        print(f'formated_players ln C40 : {formated_players}') 
        for data_dict in range(len(formated_players)): 
            player_x = Player(  # player_model. 
                lastname=formated_players[data_dict]['lastname'], 
                firstname=formated_players[data_dict]['firstname'], 
                birthdate=formated_players[data_dict]['birthdate'], 
                genre=formated_players[data_dict]['genre'], 
                classement=formated_players[data_dict]['classement']
            ) 

            print('player_x ln C50 :  {player_x}') 
            players.append(player_x) 
        print('players ln C52 :  {players}') 
        
        return players 


        # pour débug 
        # count_players += 1 if isinstance(player_x, player_model.Player) else count_players 
        # if count_players > 1: 
        #     print(f'There is {count_players} subscribers to the chess tournament') 
        # else: 
        #     print(f'There is {count_players} subscriber to the chess tournament') 


    def serialize_multi_players(players): 
        # global serialize_one_player(players)  # ??? 
        serialized_players = [] 

        print(f'players C64 : {players}') 

        # for p_obj in range(len(players)): 
        #     print(f'p_obj : {p_obj}\n') 
        #     p_serial = Player.serialize_one_player( 
        #         'lastname': players[p_obj].lastname, 
        #         'firstname': players[p_obj].firstname, 
        #         'birthdate': players[p_obj].birthdate, 
        #         'genre': players[p_obj].genre, 
        #         'classement': players[p_obj].classement 
        #     ) 
        #     # print('p_serial : ', p_serial) 
        # serialized_players.append(p_serial) 

        # print(f'type players ln M101 : {type(players)}') 
        # print(f'type players[0] ln M101 : {type(players[0])}') 
        print(f'players ln M93 : {players}') 

        for p_obj in range(len(players)): 

            print(f'type(p_obj) : {type(p_obj)}\n') 
            print(f'p_obj : {p_obj}\n') 
            print(f'players[{p_obj}] : {players[p_obj]}\n') 

            serialized_player_data = {
                'lastname': players[p_obj].lastname, 
                'firstname': players[p_obj].firstname, 
                'birthdate': players[p_obj].birthdate, 
                'genre': players[p_obj].genre, 
                'classement': players[p_obj].classement 
            } 

            serialized_players.append(serialized_player_data) 

        print(f'serialized_players ln M111 : {players}') 

        return serialized_players 


