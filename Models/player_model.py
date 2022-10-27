



# TinyDB 
from tinydb import TinyDB

# from Controllers.player_controller import Register_player

# from Controllers import player_controller
# from Views.get_player_data import Player_prompt_view 

# TinyDB 
db = TinyDB('db.json') 
players_table = db.table('players') 



class Player(): 

    def __init__(self, lastname, firstname, birthdate, genre, classement): 
        self.lastname = lastname  
        self.firstname = firstname 
        self.birthdate = birthdate 
        self.genre = genre 
        self.classement = classement 


    def __str__(self): 
        born = '' 
        if self.genre == 'M': 
            born = 'né'
        elif self.genre == 'F': 
            born = 'née' 
        elif self.genre == 'O': 
            born = 'né.e' 
        return f'{self.firstname} {self.lastname} {born} on {self.birthdate}, place: {self.classement}.' 


    # players = player_controller.Register_player.instantiate_players(
    #     player_controller.Register_player.formated_players_data
    # ) 



    # def serialize_one_player(players): 
    # # def serialize_one_player(lastname, firstname, birthdate, genre, classement): 
    #     """ Serialize one player in order to register it in the DB """ 

    #     serialized_player_data = {
    #         'lastname': players['lastname'], 
    #         'firstname': players['firstname'], 
    #         'birthdate': players['birthdate'], 
    #         'genre': players['genre'], 
    #         'classement': players['classement'] 
    #     } 

    #     return serialized_player_data 


    # Liste des dictionnaires de données récupérées via le prompt 
    # players_data = Dashboard_view.prompt_for_players_data() 
    # pour débug 
    # for pd in range(len(players_data)): 
    #     # print(f'pd : {pd}\n') 
    #     print(f'players_data[{pd}] : ', players_data[pd]) 
    #     print('\n') 
    # formated_players_data = Dashboard_view.formate_data(players_data) 

    # players = player_controller.Register_player.instantiate_players(
    #     Player_prompt_view.formated_players
    # ) 



    # def serialize_multi_players(players): 
    #     # global serialize_one_player(players)  # ??? 
    #     serialized_players = [] 

    #     print(f'players : {players}') 

    #     # for p_obj in range(len(players)): 
    #     #     print(f'p_obj : {p_obj}\n') 
    #     #     p_serial = Player.serialize_one_player( 
    #     #         'lastname': players[p_obj].lastname, 
    #     #         'firstname': players[p_obj].firstname, 
    #     #         'birthdate': players[p_obj].birthdate, 
    #     #         'genre': players[p_obj].genre, 
    #     #         'classement': players[p_obj].classement 
    #     #     ) 
    #     #     # print('p_serial : ', p_serial) 
    #     # serialized_players.append(p_serial) 

    #     # print(f'type players ln M101 : {type(players)}') 
    #     # print(f'type players[0] ln M101 : {type(players[0])}') 
    #     print(f'players ln M93 : {players}') 

    #     for p_obj in range(len(players)): 

    #         print(f'type(p_obj) : {type(p_obj)}\n') 
    #         print(f'p_obj : {p_obj}\n') 
    #         print(f'players[{p_obj}] : {players[p_obj]}\n') 

    #         serialized_player_data = {
    #             'lastname': players[p_obj].lastname, 
    #             'firstname': players[p_obj].firstname, 
    #             'birthdate': players[p_obj].birthdate, 
    #             'genre': players[p_obj].genre, 
    #             'classement': players[p_obj].classement 
    #         } 

    #     serialized_players.append(serialized_player_data) 

    #     print(f'serialized_players ln M111 : {players}') 

    #     return serialized_players 


    # # Liste pour les joueurs sérialisés 
    # serialized_players = serialize_multi_players(players) 

    # serialized_players = Register_player.instantiate_players 

    # # # Enregistrer les joueurs sérialisés dans la bdd : 
    # players_table.truncate() 
    # # # players_table.insert(player1) # for 1 player 
    # players_table.insert_multiple(serialized_players) 

