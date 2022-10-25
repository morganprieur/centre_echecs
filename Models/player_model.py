


from Controllers.players_controller import Register_players 

# TinyDB 
from tinydb import TinyDB 

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
        if self.genre == 'garçon': 
            born = 'né'
        elif self.genre == 'fille': 
            born = 'née' 
        return f'{self.firstname} {self.lastname} {born} on {self.birthdate}, place: {self.classement}.' 

    # Pas besoin de méthode spécifique pour saisir les joueurs, 
    # on les ajoute manuellement depuis la console 


    # players = Register_players.instantiate_players(Register_players.formated_players_data) 

    def serialize_one_player(players): 
    # def serialize_one_player(lastname, firstname, birthdate, genre, classement): 
        """ Serialize one player in order to register it in the DB """ 

        serialized_player_data = {
            'lastname': players['lastname'], 
            'firstname': players['firstname'], 
            'birthdate': players['birthdate'], 
            'genre': players['genre'], 
            'classement': players['classement'] 
        } 

        return serialized_player_data 


    # Liste des dictionnaires de données récupérées via le prompt 
    # players_data = Dashboard_view.prompt_for_players_data() 
    # pour débug 
    # for pd in range(len(players_data)): 
    #     # print(f'pd : {pd}\n') 
    #     print(f'players_data[{pd}] : ', players_data[pd]) 
    #     print('\n') 
    # formated_players_data = Dashboard_view.formate_data(players_data) 

    # players = instantiate_players(formated_players_data) 


    def serialize_multi_players(serialized_player_data, players): 
    # def serialize_multi_players(players): 
        # global serialize_one_player(players)  # ??? 
        serialized_players = [] 

        # players 

        for p_obj in range(len(serialized_player_data)): 
            # print(f'p_obj : {p_obj}\n') 
            p_serial = Register_players.serialize_one_player(              # ??? 
                lastname=serialized_player_data[p_obj].lastname, 
                firstname=serialized_player_data[p_obj].firstname, 
                birthdate=serialized_player_data[p_obj].birthdate, 
                genre=serialized_player_data[p_obj].genre, 
                classement=serialized_player_data[p_obj].classement
            ) 
            # print('p_serial : ', p_serial) 
        serialized_players.append(p_serial) 

        # return serialized_players 


    # Liste pour les joueurs sérialisés 
    serialized_players = serialize_multi_players(players) 


    # Enregistrer les joueurs sérialisés dans la bdd : 
    players_table.truncate() 
    # players_table.insert(player1) # for 1 player 
    players_table.insert_multiple(serialized_players) 

