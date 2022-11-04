


from Views.get_player_view import Get_player_view 
from Models.player_model import Player 

import re 



class Player_controller(): 


    # dashboard 
    # welcome = Dashboard_view.welcome_view(Dashboard_view) 

    def start(): 
        # players 
        print('start') 
        formated_players = Get_player_view.get_many_players() 
        players = Player.instantiate_players(formated_players) 
        # serialized_players = 
        Player.serialize_multi_players(players) 
        # print(f'serialized_players[0]["lastname"] ln51 : {serialized_players[0]["lastname"]}') 
        # print(f'serialized_players[1]["lastname"] ln51 : {serialized_players[1]["lastname"]}') 
    

    # def instantiate_players(formated_players): 
    #     """ Instantiate the players in a list of object Players. 
    #     Args:
    #         formated_players (list): the list of the players formated data 
    #     Returns:
    #         players (list): the players in form of object Player 
    #     """ 
    #     # Liste pour les joueurs objets 
    #     players = [] 

    #     print(f'formated_players ln C23 : {formated_players}')  # inversés 

    #     for data_dict in range(len(formated_players)): 
    #         player_x = Player( 
    #             lastname=formated_players[data_dict]['lastname'], 
    #             firstname=formated_players[data_dict]['firstname'], 
    #             birthdate=formated_players[data_dict]['birthdate'], 
    #             genre=formated_players[data_dict]['genre'], 
    #             classement=formated_players[data_dict]['classement']
    #         ) 
    #         print(f'player_x ln C34 :  {player_x}') 

    #         players.append(player_x) 

    #     print(f'players ln C38 :  {players}') 
    #     print(f'players ln C38 :  {players[0].lastname}')  # inversés 
        
    #     return players 


    # def serialize_multi_players(players): 
    #     """ Serialization of the players data in order to register them 
    #         in the DB. 
    #     Args:
    #         players (list): list of object Players 
    #     Returns:
    #         serialized_players (list): the players in the expected format for the DB 
    #     """
    #     serialized_players = [] 

    #     # print(f'players C48 : {players}')   # inversés 
    #     # print(f'players C48 : {players[0].lastname}') 
    #     for p_obj in range(len(players)): 
    #         # print(f'type(p_obj) : {type(p_obj)}\n') 
    #         # print(f'p_obj : {p_obj}\n') 
    #         # print(f'players[{p_obj}] : {players[p_obj]}\n') 
    #         serialized_player_data = {
    #             'lastname': players[p_obj].lastname, 
    #             'firstname': players[p_obj].firstname, 
    #             'birthdate': players[p_obj].birthdate, 
    #             'genre': players[p_obj].genre, 
    #             'classement': players[p_obj].classement 
    #         } 

    #         serialized_players.append(serialized_player_data) 

    #     print(f'serialized_players C69 : {serialized_players}')  # inversés 

    #     return serialized_players 


