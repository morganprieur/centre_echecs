from cmd import PROMPT
from Models import player_model 
# functions 
from utils.functions import prompt_for_players_data, serialize_player 

# TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
players_table = db.table('players') 


#TODO : 
# Au début de la saisie, demander combien de joueurs on doit enregistrer
# -> stocker ce nb dans une variable 
# -> stocker le nb de joueurs déjà enregistrés dans une autre variable (initialisée à 0) 
# 
# Initialiser une liste players_data[] pour stocker les données par joueur 
# 
# boucler tant que les joueurs qui rentent à enregistrer ne sont pas à 0 : 
#   questions prompts 
#   stocker chaque data dans un dictionnaire 
# 
#   ajouter ce dict à la liste players_data 
#   incrémenter la variable du nb de joueurs enregsitrés 
#   décrémenter la variable du nb de joueurs à enregistrer 
# 
# Récupérer la liste des données des joueurs 
# Initialiser une liste pour les joueurs objets 
# Boucler dans la liste des données des joueurs pour les instancier comme player_model.Player : 
#   Les stocker dans la liste des joueurs objets 
# 
# Initialiser une liste pour les joueurs sérialisés 
# Boucler dans la liste des joueurs objets : 
#   les sérialiser 
#   les stocker dans la liste des joueurs sérialisés 
# 
# Charger les joueurs sérialisés dans la DB 
# 

# Liste des dictionnaires de données récupérées via le prompt 
players_data = prompt_for_players_data() 
# pour débug 
for pd in players_data: 
    print('\n') 
    print(f'players_data[{pd}] : ', players_data) 

# Liste pour les joueurs objets 
players = [] 
# pour débug 
count_players = 0 

for data_dict in range(len(players_data)): 
    print(f'x : {data_dict}\n') 
    player_x = player_model.Player(
        lastname = players_data[data_dict]['ask_for_lastname'], 
        firstname = players_data[data_dict]['ask_for_firstname'], 
        birthdate = players_data[data_dict]['ask_for_birthdate'], 
        genre = players_data[data_dict]['ask_for_genre'], 
        classement = players_data[data_dict]['ask_for_classement']
    ) 
    print('player_x : ', player_x) 
    players.append(player_x) 

    # pour débug 
    count_players += 1 if isinstance(player_x, player_model.Player) else count_players 

    if count_players > 1: 
        print(f'There is {count_players} subscribers to the chess tournament') 
    else: 
        print(f'There is {count_players} subscriber to the chess tournament') 

print('\n') 
print('players : ', players) 



# liste pour les joueurs sérilisés 
serialized_players = [] 

for po in range(len(players)): 
    print(f'po : {po}\n') 
    player_s = serialize_player( 
        lastname = players[po].lastname, 
        firstname = players[po].firstname, 
        birthdate = players[po].birthdate, 
        genre = players[po].genre, 
        classement = players[po].classement
    ) 
    print('player_s : ', player_s) 
    serialized_players.append(player_s) 


# Charger les joueurs sérialisés dans la bdd : 
players_table.truncate() 
# players_table.insert(player1) 
players_table.insert_multiple(serialized_players) 


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






