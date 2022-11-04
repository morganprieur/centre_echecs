



from Views.get_player_view import Get_player_view 
from Models.match_model import Match 
from Models.player_model import Player 

import re 

# TinyDB 
from tinydb import TinyDB, Query 
db = TinyDB('db.json') 
players_table = db.table('players') 


class Player_controller(): 



    def start(): 
        print('start') 
        # players 
        # formated_players = Get_player_view.get_many_players() 
        # players = Player.instantiate_players(formated_players) 
        # serialized_players = Player.serialize_multi_players(players) 

        # matches
        # match_y = Match.instantiate_match() 
        p_table_class = Player_controller.sort_players_by_classement() 
        half_1, half_2 = Player_controller.separate_players_in_2_halfs(p_table_class) 
        matches = Player_controller.associate_players_for_round_1(half_1, half_2) 
        matches_obj = Player_controller.instantiate_matches(matches) 

    # Associer les joueurs pour chaque match du tour 1 
    def sort_players_by_classement():   # Player 
        # trier les joueurs par classement 
        p_table = players_table.all() 
        # print(f'p_table C36 : {p_table}') 
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
    #       ...
    # ] 

        # 1 a = {"key1": 5 , "key2": 8, "key3": 2}
        # 2 b = {"key1": 7 , "key2": 4, "key3": 9}
        # 3 c = {"key1": 6 , "key2": 1, "key3": 1}
        # 4 undecorated = [a, b, c] # how do you sort this list?
        # 1 sort_on = "key2"
        # 2 decorated = [(dict_[sort_on], dict_) for dict_ in undecorated]
        # 3 decorated.sort()
        # 4 result = [dict_ for (key, dict_) in decorated] 
        sort_on = 'classement' 
        decorated = [(dict_[sort_on], dict_) for dict_ in p_table] 
        decorated.sort() 
        result = [dict_ for (key, dict_) in decorated] 
        # print(f'result C70 : {result}') 

        return result 
    # sort_players_by_classement(Player) 

    # def get_players_ids(p_table_class): 
    def separate_players_in_2_halfs(p_table_class): 
        # séparer les joueurs en 2 moitiés 
        half_1 = [] 
        half_2 = [] 
        # Item = Query()
        # p_table_class = db.search(Item['lastname'] == .) 
        p_table = players_table.all() 
        for i in range(len(p_table_class)): 
            # print(f'p_table_class[i].doc_id C87 : {p_table_class[i].doc_id}') 
            print(f'p_table_class[i] C88 : {p_table_class[i]}') 
            if i < len(p_table_class)/2: 
                print(i) 
                half_1.append(p_table_class[i]) 
            if len(p_table_class)/2 <= i: 
                print(i) 
                half_2.append(p_table_class[i]) 
        print(f'half_1 C95 : {half_1}') 
        print(f'half_2 C96 : {half_2}') 

        return half_1, half_2 

        # utiliser l'id des joueurs 
        # créer tuples (player_id, score=0) pour chaque joueur 

    def associate_players_for_round_1(half_1, half_2): 
        # associer chaque rang de chaque moitié 
        print(f'half_1 : {half_1}') 
        print(f'half_2 : {half_2}') 
        # for i in half_1: 
        for i in range(len(half_1)): 
            print(f'half_1[i].doc_id C108 : {half_1[i].doc_id}') 
        for i in range(len(half_2)): 
            print(f'half_2[i].doc_id C111 : {half_2[i].doc_id}') 
        tuples = [] 
        tuple_1 = (half_1[0].doc_id, 0) 
        tuple_2 = (half_1[1].doc_id, 0) 
        tuple_3 = (half_1[2].doc_id, 0) 
        tuple_4 = (half_1[3].doc_id, 0) 
        tuple_5 = (half_2[0].doc_id, 0) 
        tuple_6 = (half_2[1].doc_id, 0) 
        tuple_7 = (half_2[2].doc_id, 0) 
        tuple_8 = (half_2[3].doc_id, 0) 
        tuples.append(tuple_1) 
        tuples.append(tuple_2) 
        tuples.append(tuple_3) 
        tuples.append(tuple_4) 
        tuples.append(tuple_5) 
        tuples.append(tuple_6) 
        tuples.append(tuple_7) 
        tuples.append(tuple_8) 
        print(f'tuples : {tuples}') 

        # associer les tuples 
        match_1 = [] 
        match_2 = [] 
        match_3 = [] 
        match_4 = [] 
        match_1.append(tuple_1) 
        match_1.append(tuple_2) 
        match_2.append(tuple_3) 
        match_2.append(tuple_4) 
        match_3.append(tuple_5) 
        match_3.append(tuple_6) 
        match_4.append(tuple_7) 
        match_4.append(tuple_8) 

        print(f'match_1 : {match_1}') 
        print(f'match_2 : {match_2}') 
        print(f'match_3 : {match_3}') 
        print(f'match_4 : {match_4}') 

        matches = [] 
        matches.append(match_1) 
        matches.append(match_2) 
        matches.append(match_3) 
        matches.append(match_4) 

        return matches 


    def instantiate_matches(matches): 
        # instancier les matches 
        matches_obj = [] 
        for m in range(len(matches)): 
            match_y = Match( 
                tuple_match=matches[m] 
            ) 
            matches_obj.append(match_y) 
        print(f'matches_obj : {matches_obj}')  

