



from Models.player_model import Player 

import re 

# TinyDB 
# from tinydb import TinyDB 
# db = TinyDB('db.json') 
# players_table = db.table('players') 



class Register_player(): 

    def instantiate_players(formated_players): 

        # Liste pour les joueurs objets 
        players = [] 

        print(f'formated_players ln C23 : {formated_players}') 

        for data_dict in range(len(formated_players)): 
        
            player_x = Player(  # player_model. 
                lastname=formated_players[data_dict]['lastname'], 
                firstname=formated_players[data_dict]['firstname'], 
                birthdate=formated_players[data_dict]['birthdate'], 
                genre=formated_players[data_dict]['genre'], 
                classement=formated_players[data_dict]['classement']
            ) 
            print('player_x ln C34 :  {player_x}') 

            players.append(player_x) 

        print('players ln C38 :  {players}') 
        
        return players 



    def serialize_multi_players(players): 

        serialized_players = [] 

        print(f'players C48 : {players}') 

        for p_obj in range(len(players)): 

            # print(f'type(p_obj) : {type(p_obj)}\n') 
            # print(f'p_obj : {p_obj}\n') 
            # print(f'players[{p_obj}] : {players[p_obj]}\n') 

            serialized_player_data = {
                'lastname': players[p_obj].lastname, 
                'firstname': players[p_obj].firstname, 
                'birthdate': players[p_obj].birthdate, 
                'genre': players[p_obj].genre, 
                'classement': players[p_obj].classement 
            } 

            serialized_players.append(serialized_player_data) 

        print(f'serialized_players ln M66 : {serialized_players}') 

        return serialized_players 


