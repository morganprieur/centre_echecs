from Models import player_model 
# functions 
from utils.functions import prompt_for_players_data, serialize_multi_players  # , serialize_one_player 

# TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
players_table = db.table('players') 


class Register_players(): 

    # """
        # >>> data_dict(player_x = player_model.Player(
            #     lastname = 'nom', 
            #     firstname = 'prénom', 
            #     birthdate = '2022-10-06', 
            #     genre = 'M', 
            #     classement = 102
            # )
    #     3
    #     >>> to_absolute(-4)
    #     4
    #     """
    #     if number < 0: 
    #         return -number 
    #     else: 
    #         return number 
    # Liste des dictionnaires de données récupérées via le prompt 
    players_data = prompt_for_players_data() 
    # pour débug 
    for pd in range(len(players_data)): 
        print(f'pd : {pd}\n') 
        print(f'players_data[{pd}] : ', players_data[pd]) 
        print('\n') 

    # Liste pour les joueurs objets 
    players = [] 
    # pour débug 
    # count_players = 0 

    for data_dict in range(len(players_data)): 
        player_x = player_model.Player(
            lastname = players_data[data_dict]['lastname'], 
            firstname = players_data[data_dict]['firstname'], 
            birthdate = players_data[data_dict]['birthdate'], 
            genre = players_data[data_dict]['genre'], 
            classement = players_data[data_dict]['classement']
        ) 
        # print('player_x : ', player_x) 
        players.append(player_x) 

        # pour débug 
        # count_players += 1 if isinstance(player_x, player_model.Player) else count_players 
        # if count_players > 1: 
        #     print(f'There is {count_players} subscribers to the chess tournament') 
        # else: 
        #     print(f'There is {count_players} subscriber to the chess tournament') 

    # print('players : ', players) 
    # print('\n') 


    # Liste pour les joueurs sérialisés 
    serialized_players = serialize_multi_players(players) 


    # Enregistrer les joueurs sérialisés dans la bdd : 
    players_table.truncate() 
    # players_table.insert(player1) # for 1 player 
    players_table.insert_multiple(serialized_players) 




# liste pour les joueurs sérialisés 
# serialized_players = [] 

# for p_obj in range(len(players)): 
#     print(f'p_obj : {p_obj}\n') 
#     p_serial = serialize_player( 
#         lastname = players[p_obj].lastname, 
#         firstname = players[p_obj].firstname, 
#         birthdate = players[p_obj].birthdate, 
#         genre = players[p_obj].genre, 
#         classement = players[p_obj].classement
#     ) 
#     print('p_serial : ', p_serial) 
#     serialized_players.append(p_serial) 





# if(len(players_data)) == 1: 

#     # Reçus de la réponse au prompt : 
#     player1 = player_model.Player(
#         lastname = players_data[0]['ask_for_lastname'], 
#         firstname = players_data[0]['ask_for_firstname'], 
#         birthdate = players_data[0]['ask_for_birthdate'], 
#         genre = players_data[0]['ask_for_genre'], 
#         classement = players_data[0]['ask_for_classement'] 
#     ) 
#     print(player1) 

# elif len(players_data) == 2: 
#         # Reçus de la réponse au prompt : 
#     player1 = player_model.Player(
#         lastname = players_data[0]['ask_for_lastname'], 
#         firstname = players_data[0]['ask_for_firstname'], 
#         birthdate = players_data[0]['ask_for_birthdate'], 
#         genre = players_data[0]['ask_for_genre'], 
#         classement = players_data[0]['ask_for_classement'] 
#     )
#     player2 = player_model.Player(
#         lastname = players_data[1]['ask_for_lastname'], 
#         firstname = players_data[1]['ask_for_firstname'], 
#         birthdate = players_data[1]['ask_for_birthdate'], 
#         genre = players_data[1]['ask_for_genre'], 
#         classement = players_data[1]['ask_for_classement'] 
#     ) 
#     print('\n') 
#     print(player1) 
#     print('\n') 
#     print(player2) 
#     print('\n') 

# oren = player_model.Player(
#     'Prieur', 'Oren', '2009-03-25', 'garçon', 70
# ) 
# chris = player_model.Player(
#     'Prieur', 'Chris', '1974-01-22', 'garçon', 68
# ) 

# player1 = serialize_player(
#     players[0].lastname, 
#     players[0].firstname, 
#     players[0].birthdate, 
#     players[0].genre, 
#     players[0].classement 
# ) 
# player2 = serialize_player(
#     players[1].lastname, 
#     players[1].firstname, 
#     players[1].birthdate, 
#     players[1].genre, 
#     players[1].classement 
# ) 

# For charging some players in the DB : 
# serialized_players = [ 
#     player1, player2 
# ] 






