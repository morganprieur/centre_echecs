from cmd import PROMPT
from Models import player_model 
# functions 
from utils.functions import prompt_for_players_data, serialize_player 

# TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
players_table = db.table('players') 




#TODO : 
# Ala fin des prompts pour les données d'un joueur, 
# demander si on vue tenregistrer un nouveau joueur. 
# Si oui: on relance la fonction prompt_for_one_player(), 
# sinon on sort. 
# Chaque jeu de données doit être enregistré dans un objet Player, 
# stocké dans cette liste : 
# Make a list of the players data 

players_data = prompt_for_players_data() 
# players_data_list = player_data # marche pas, il faut plusieurs jeux de data 

if(len(players_data)) == 1: 

    # Reçus de la réponse au prompt : 
    player1 = player_model.Player(
        lastname = players_data[0]['ask_for_lastname'], 
        firstname = players_data[0]['ask_for_firstname'], 
        birthdate = players_data[0]['ask_for_birthdate'], 
        genre = players_data[0]['ask_for_genre'], 
        classement = players_data[0]['ask_for_classement'] 
    ) 
    print(player1) 

elif len(players_data) == 2: 
        # Reçus de la réponse au prompt : 
    player1 = player_model.Player(
        lastname = players_data[0]['ask_for_lastname'], 
        firstname = players_data[0]['ask_for_firstname'], 
        birthdate = players_data[0]['ask_for_birthdate'], 
        genre = players_data[0]['ask_for_genre'], 
        classement = players_data[0]['ask_for_classement'] 
    )
    player2 = player_model.Player(
        lastname = players_data[1]['ask_for_lastname'], 
        firstname = players_data[1]['ask_for_firstname'], 
        birthdate = players_data[1]['ask_for_birthdate'], 
        genre = players_data[1]['ask_for_genre'], 
        classement = players_data[1]['ask_for_classement'] 
    ) 
    print('\n') 
    print(player1) 
    print('\n') 
    print(player2) 
    print('\n') 

# oren = player_model.Player(
#     'Prieur', 'Oren', '2009-03-25', 'garçon', 70
# ) 
# chris = player_model.Player(
#     'Prieur', 'Chris', '1974-01-22', 'garçon', 68
# ) 

count_players = 0 
count_players += 1 if isinstance(player2, player_model.Player) else count_players 

if count_players > 1: 
    print(f'There is {count_players} subscribers to the chess tournament') 
else: 
    print(f'There is {count_players} subscriber to the chess tournament') 

player1 = serialize_player(
        player1.lastname, 
        player1.firstname, 
        player1.birthdate, 
        player1.genre, 
        player1.classement 
    )
player2 = serialize_player(
    player2.lastname, 
    player2.firstname, 
    player2.birthdate, 
    player2.genre, 
    player2.classement 
) 
# player1 = serialize_player(
#     player1.lastname, 
#     player1.firstname, 
#     player1.birthdate, 
#     player1.genre, 
#     player1.classement
# ) 
# chris = serialize_player(
#     chris.lastname, chris.firstname, chris.birthdate, chris.genre, chris.classement
# ) 

# For charging some players in the DB : 
serialized_players = [ 
    player1, player2 
] 


# Charger les joueurs sérialisés dans la bdd : 
players_table.truncate() 
# players_table.insert(player1) 
players_table.insert_multiple(serialized_players) 



