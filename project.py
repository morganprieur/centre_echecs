from cmd import PROMPT
from Models import player_model 
# functions 
from utils.functions import prompt_for_one_player, serialize_player 

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

player_data = prompt_for_one_player() 
# players_data_list = player_data # marche pas, il faut plusieurs jeux de data 


# Reçus de la réponse au prompt : 
player1 = player_model.Player(
    lastname = player_data['ask_for_lastname'], 
    firstname = player_data['ask_for_firstname'], 
    birthdate = player_data['ask_for_birthdate'], 
    genre = player_data['ask_for_genre'], 
    classement = player_data['ask_for_classement'] 
) 
# oren = player_model.Player(
#     'Prieur', 'Oren', '2009-03-25', 'garçon', 70
# ) 
# chris = player_model.Player(
#     'Prieur', 'Chris', '1974-01-22', 'garçon', 68
# ) 

print(player1) 

count_players = 0 
count_players += 1 if isinstance(player1, player_model.Player) else count_players 

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
# chris = serialize_player(
#     chris.lastname, chris.firstname, chris.birthdate, chris.genre, chris.classement
# ) 


# For charging some players in the DB : 
# serialized_players = [ 
#     oren, chris
# ] 


# Charger les joueurs sérialisés dans la bdd : 
players_table.truncate() 
players_table.insert(player1) 
# players_table.insert_multiple(serialized_players) 



