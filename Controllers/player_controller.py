



from Views.get_player_view import Get_player_view 
from Models.match_model import Match 
from Models.player_model import Player 

import re 

# TinyDB 
from tinydb import TinyDB, Query 
db = TinyDB('db.json') 
players_table = db.table('players') 


class Player_controller(): 

    def instantiate_players(formated_players): 
        """ Instantiate the players in a list of object Players. 
        Args:
            formated_players (list): the list of the players formated data 
        Returns:
            players (list): the players in form of object Player 
        """ 
        # Liste pour les joueurs objets 
        players = [] 

        print(f'formated_players ln C23 : {formated_players}')  # inversés 

    def start(): 
        # players 
        print('start') 
        # formated_players = Get_player_view.get_many_players() 
        # players = Player.instantiate_players(formated_players) 
        # serialized_players = Player.serialize_multi_players(players) 

        # match_y = Match.instantiate_match() 


    # Associer les joueurs pour chaque match du tour 1 
    def trier_joueurs_par_classement(Player): 
        # trier les joueurs par classement 
        # p_table = players_table.all() 
        # print(p_table) 
    # [
    #     {
    #         'lastname': 'Nom01 \n', 
    #         'firstname': 'Prã©nom01 \n', 
    #         'birthdate': '2001-10-31 \n', 
    #         'genre': 'M \n', 
    #         'classement': '44 \n'
    #     }, 
    #     {
    #         'lastname': 'Nom02 \n', 
    #         'firstname': 'Prã©nom02 \n', 
    #         'birthdate': '2002-10-31 \n', 
    #         'genre': 'F \n', 
    #         'classement': '40 \n'
    #     }
    # ] 
        # >>> Fruit = Query()
        # >>> db.search(Fruit.type == 'peach')
        # [{'count': 3, 'type': 'peach'}]
        # >>> db.search(Fruit.count > 5)
        # [{'count': 7, 'type': 'apple'}] 
        # Query().field == 2
        pl = Query() 
        pl_40 = players_table.search(pl.classement == '40 \n') 
        print(f'pl_40 : {pl_40}')  
        # dic = {} 
        # lst =[] 
        # for i in range(len(p_table)): 
        #     print(i) 
        #     print(p_table[i]) 
        #     dic[i] = p_table[i] 
        # print(f'dic : {dic}') 
            # print(type(i)) 
            # for a,b in list(i.items()): 
            #     print(b,a) 
            #     lst.append((b,a)) 
            # lst.append(i) 
        # print(dic.items()) 
        # print(f'lst : {lst}') 
        # for a,b,c,d,e in list(p_table.items()): 
        #     list.append(e,a,b,c,d) 
        # lst.sort() 
        # print(lst) 
        # for d in dic: 
        #     print(d[6]) 

    trier_joueurs_par_classement(Player) 
    
    def separer_joueurs_en_moities(): 
        # séparer les joueurs en 2 moitiés 
        pass 

    def associer_joueurs_tour_1(): 
        # associer chaque rang de chaque moitié 
        pass 
        

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
        
        return players 


    def serialize_multi_players(players): 
        """ Serialization of the players data in order to register them 
            in the DB. 
        Args:
            players (list): list of object Players 
        Returns:
            serialized_players (list): the players in the expected format for the DB 
        """
        serialized_players = [] 

        # print(f'players C48 : {players}')   # inversés 
        # print(f'players C48 : {players[0].lastname}') 
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

        print(f'serialized_players C69 : {serialized_players}')  # inversés 

        return serialized_players 


