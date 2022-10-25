



# from Models.player_model import Player 

# from Views.dashboard_view import Dashboard_view 

# functions 
# from utils.functions import prompt_for_players_data, serialize_multi_players, serialize_one_player  # , serialize_one_player 

# import re 
# from prompt_toolkit import PromptSession 
# from datetime import datetime, date 
# from tinydb import TinyDB  


# to use prompt as an instance 
# session = PromptSession() 
# TinyDB 
# db = TinyDB('db.json') 
# players_table = db.table('players') 


# class Try_controller(): 

#     print('player_controller -> try_controller') 


# class Register_players(): 




# # Vue : 
#     # def prompt_for_players_data(): 
#     #     """ Get the players data via prompt inputs in the console. 
#     #         Calls another function in order to formate the data. 
#     #     """ 

#     #     # List for the players data  
#     #     players_data = [] 

#     #     # Prompts for tournament configuration 
#     #     # ask_for_current_year = int(session.prompt('What\'s the current year ?\n')) 
#     #     # ask_for_min_age = int(session.prompt('What is the min. age ?\n')) 

#     #     ask_for_number_of_players = session.prompt('How many players left ? \n') 
#     #     players_to_register = int(ask_for_number_of_players) 
#     #     print('\nplayers_to_register (ln20) : ', players_to_register) 

#     #     while players_to_register > 0: 

#     #         # Prompt to ask the attributes of one player 
#     #         ask_for_lastname = session.prompt('Enter the player lastname: \n') 
#     #         ask_for_firstname = session.prompt('Enter the player firstname: \n') 
#     #         ask_for_birthdate = session.prompt('Enter the player birthdate (YYYY-MM-DD): \n') 
#     #         # ask_for_birth_month = session.prompt('Enter the player birth month (MM): \n') 
#     #         # ask_for_birth_year = session.prompt('Enter the player birth year (YYYY): \n') 
#     #         ask_for_genre = session.prompt('Enter the player genre (M, F, O for "other") in capitals: \n') 
#     #         ask_for_classement = int(session.prompt('Enter the player classement: \n')) 


#     #         # Formated data for one player 
#     #         player_data = { 
#     #             'lastname': ask_for_lastname, 
#     #             'firstname': ask_for_firstname, 
#     #             'birthdate': ask_for_birthdate, 
#     #             'genre': ask_for_genre, 
#     #             'classement': ask_for_classement 
#     #         } 
#     #         players_data.append(player_data) 

#     #         players_to_register -= 1 
#     #         print('\nplayers_to_register (ln64) : ', players_to_register) 

#     #     return players_data 



#     # def formate_data(players_data): 

#     #     formated_players_data = {} 

#     #     # formate data 
#     #     formated_players_data['lastname'] = players_data['ask_for_lastname'].capitalize() 
#     #     formated_players_data['firstname'] = players_data['ask_for_firstname'].capitalize() 

#     #     # lastname = ask_for_lastname.capitalize() 
#     #     # firstname = ask_for_firstname.capitalize() 

#     #     # annee_en_cours = ask_for_current_year 
#     #     # age_mini = ask_for_min_age 

#     #     # formate birthdate 
#     #     if re.search('\d\d\d\d[-\d\d]+', players_data['ask_for_birthdate']): 
#     #         # print(re.search('\d\d\d\d[-\d\d]+', ask_for_birthdate)) 
#     #         formated_players_data['birthdate'] = players_data['ask_for_birthdate'] 
#     #         print(f'birthdate : {formated_players_data["birthdate"]}') 
#     #     else: 
#     #         formated_players_data['birthdate'] = session.prompt('Enter the player birthdate (YYYY-MM-DD): \n') 
#     #         print(f'ask_for_birthdate : {formated_players_data["birthdate"]}') 

#     #     # formate genre 
#     #     if (players_data['ask_for_genre'] == 'M') | (players_data['ask_for_genre'] == 'F') | (players_data['ask_for_genre'] == 'O'): 
#     #         formated_players_data['genre'] = players_data['ask_for_genre'] 
#     #     else: 
#     #         formated_players_data['genre'] = session.prompt(
#     #             'Unknown letter. Enter the player genre: M, F, O (for "other") in capitals: \n'
#     #         ) 
        
#     #     formated_players_data['classement'] = players_data['ask_for_classement'] 


#     #     return formated_players_data 

#     # """
#     # >>> data_dict(player_x = player_model.Player(
#     #     lastname = 'nom', 
#     #     firstname = 'prénom', 
#     #     birthdate = '2022-10-06', 
#     #     genre = 'M', 
#     #     classement = 102
#     # )
#     #     3
#     #     >>> to_absolute(-4)
#     #     4
#     #     """
#     #     if number < 0: 
#     #         return -number 
#     #     else: 
#     #         return number 



# # Contrôleur : 

#     # formated_players_data = Dashboard_view.formate_data(players_data=Dashboard_view.prompt_for_players_data()) 
#     players_data = Dashboard_view.prompt_for_players_data() 

#     def instantiate_players(formated_players_data): 

#         # Liste pour les joueurs objets 
#         players = [] 
#         # pour débug 
#         # count_players = 0 

#         for data_dict in range(len(formated_players_data)): 
#             player_x = Player(
#                 lastname=formated_players_data[data_dict]['lastname'], 
#                 firstname=formated_players_data[data_dict]['firstname'], 
#                 birthdate=formated_players_data[data_dict]['birthdate'], 
#                 genre=formated_players_data[data_dict]['genre'], 
#                 classement=formated_players_data[data_dict]['classement']
#             ) 
#             # print('player_x : ', player_x) 
#             players.append(player_x) 
        
#         return players 



#         # pour débug 
#         # count_players += 1 if isinstance(player_x, player_model.Player) else count_players 
#         # if count_players > 1: 
#         #     print(f'There is {count_players} subscribers to the chess tournament') 
#         # else: 
#         #     print(f'There is {count_players} subscriber to the chess tournament') 

#     # print('players : ', players) 
#     # print('\n') 


#     # Liste des dictionnaires de données récupérées via le prompt 
#     player_data = Dashboard_view.prompt_for_players_data() 
#     # pour débug 
#     for pd in range(len(player_data)): 
#         # print(f'pd : {pd}\n') 
#         print(f'player_data[{pd}] : ', player_data[pd]) 
#         print('\n') 
#     formated_player_data = Dashboard_view.formate_data(player_data) 

#     players = instantiate_players(formated_player_data) 

#     # players = Register_players.instantiate_players(Register_players.formated_players_data) 


# # modèle : 

#     # def serialize_one_player(players): 
#     # # def serialize_one_player(lastname, firstname, birthdate, genre, classement): 
#     #     """ Serialize one player in order to register it in the DB """ 

#     #     serialized_player_data = {
#     #         'lastname': players['lastname'], 
#     #         'firstname': players['firstname'], 
#     #         'birthdate': players['birthdate'], 
#     #         'genre': players['genre'], 
#     #         'classement': players['classement'] 
#     #     } 

#     #     return serialized_player_data 




#     # def serialize_multi_players(serialized_player_data, players): 
#     # # def serialize_multi_players(players): 
#     #     # global serialize_one_player(players)  # ??? 
#     #     serialized_players = [] 

#     #     # players 

#     #     for p_obj in range(len(serialized_player_data)): 
#     #         # print(f'p_obj : {p_obj}\n') 
#     #         p_serial = Register_players.serialize_one_player(              # ??? 
#     #             lastname=serialized_player_data[p_obj].lastname, 
#     #             firstname=serialized_player_data[p_obj].firstname, 
#     #             birthdate=serialized_player_data[p_obj].birthdate, 
#     #             genre=serialized_player_data[p_obj].genre, 
#     #             classement=serialized_player_data[p_obj].classement
#     #         ) 
#     #         # print('p_serial : ', p_serial) 
#     #     serialized_players.append(p_serial) 

#     #     # return serialized_players 


#     # # Liste pour les joueurs sérialisés 
#     # serialized_players = serialize_multi_players(players) 


#     # # Enregistrer les joueurs sérialisés dans la bdd : 
#     # players_table.truncate() 
#     # # players_table.insert(player1) # for 1 player 
#     # players_table.insert_multiple(serialized_players) 







# # liste pour les joueurs sérialisés 
# # serialized_players = [] 

# # for p_obj in range(len(players)): 
# #     print(f'p_obj : {p_obj}\n') 
# #     p_serial = serialize_player( 
# #         lastname = players[p_obj].lastname, 
# #         firstname = players[p_obj].firstname, 
# #         birthdate = players[p_obj].birthdate, 
# #         genre = players[p_obj].genre, 
# #         classement = players[p_obj].classement
# #     ) 
# #     print('p_serial : ', p_serial) 
# #     serialized_players.append(p_serial) 

# # if(len(players_data)) == 1: 

# #     # Reçus de la réponse au prompt : 
# #     player1 = player_model.Player(
# #         lastname = players_data[0]['ask_for_lastname'], 
# #         firstname = players_data[0]['ask_for_firstname'], 
# #         birthdate = players_data[0]['ask_for_birthdate'], 
# #         genre = players_data[0]['ask_for_genre'], 
# #         classement = players_data[0]['ask_for_classement'] 
# #     ) 
# #     print(player1) 

# # elif len(players_data) == 2: 
# #         # Reçus de la réponse au prompt : 
# #     player1 = player_model.Player(
# #         lastname = players_data[0]['ask_for_lastname'], 
# #         firstname = players_data[0]['ask_for_firstname'], 
# #         birthdate = players_data[0]['ask_for_birthdate'], 
# #         genre = players_data[0]['ask_for_genre'], 
# #         classement = players_data[0]['ask_for_classement'] 
# #     )
# #     player2 = player_model.Player(
# #         lastname = players_data[1]['ask_for_lastname'], 
# #         firstname = players_data[1]['ask_for_firstname'], 
# #         birthdate = players_data[1]['ask_for_birthdate'], 
# #         genre = players_data[1]['ask_for_genre'], 
# #         classement = players_data[1]['ask_for_classement'] 
# #     ) 
# #     print('\n') 
# #     print(player1) 
# #     print('\n') 
# #     print(player2) 
# #     print('\n') 

# # oren = player_model.Player(
# #     'Prieur', 'Oren', '2009-03-25', 'garçon', 70
# # ) 
# # chris = player_model.Player(
# #     'Prieur', 'Chris', '1974-01-22', 'garçon', 68
# # ) 

# # player1 = serialize_player(
# #     players[0].lastname, 
# #     players[0].firstname, 
# #     players[0].birthdate, 
# #     players[0].genre, 
# #     players[0].classement 
# # ) 
# # player2 = serialize_player(
# #     players[1].lastname, 
# #     players[1].firstname, 
# #     players[1].birthdate, 
# #     players[1].genre, 
# #     players[1].classement 
# # ) 

# # For charging some players in the DB : 
# # serialized_players = [ 
# #     player1, player2 
# # ] 






