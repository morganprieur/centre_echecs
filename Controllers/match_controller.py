


from Models.match_model import Match 
from Views.get_match_view import Get_match_view 

# TinyDB 
from tinydb import TinyDB, Query 
db = TinyDB('db.json') 
players_table = db.table('players') 


class Match_controller(): 

    def start(): 
        print('start matches') 
    
        matches_0_start = Match_controller.matches_start() 
        # print(f'matches_0_start C26 : {matches_0_start}')  # = M49 
        matches_1_start = Match_controller.matches_round_1(matches_0_start) 

    
    # matches
    def matches_start(): 
        p_table_class = Match_controller.sort_players_by_classement() 
        half_1, half_2 = Match_controller.separate_players_in_2_halfs(p_table_class) 
        matches_start = Match_controller.associate_players_for_round_1(half_1, half_2) 
        matches_obj_start = Match.instantiate_matches(matches_start) 
        serialized_matches_start = Match.serialize_multi_matches(matches_obj_start) 
        return matches_obj_start 
        

    ## round 1 
    def matches_round_1(matches_obj_start): 
        score_player_1_start = Get_match_view.register_scores_round_1(matches_obj_start) 
        print(f'score_player_1_round_1 C36 : {score_player_1_start}') 

        # scores_round_1_obj = Match.instantiate_scores_round_1(score_player_1_start) 

        
    

    
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
            # print(f'p_table_class[i] C88 : {p_table_class[i]}') 
            if i < len(p_table_class)/2: 
                # print(i) 
                half_1.append(p_table_class[i]) 
            if len(p_table_class)/2 <= i: 
                # print(i) 
                half_2.append(p_table_class[i]) 
        # print(f'half_1 C95 : {half_1}') 
        # print(f'half_2 C96 : {half_2}') 

        return half_1, half_2 

        # utiliser l'id des joueurs 
        # créer tuples (player_id, score=0) pour chaque joueur 

    def associate_players_for_round_1(half_1, half_2): 
        # associer chaque rang de chaque moitié 
        # print(f'half_1 : {half_1}') 
        # print(f'half_2 : {half_2}') 
        
        tuples = [] 
        for i in range(len(half_1)): 
            # print(f'half_1[i].doc_id C108 : {half_1[i].doc_id}') 
            tuples.append((half_1[i].doc_id, 0)) 
        for i in range(len(half_2)): 
            # print(f'half_2[i].doc_id C111 : {half_2[i].doc_id}') 
            tuples.append((half_2[i].doc_id, 0)) 
            # eval(f"tuple_{i}") = ({half_1[i].doc_id}, 0) 
        print(f'tuples : {tuples}') 
        # print(f'len(tuples) : {len(tuples)}') 

        # associer les tuples dans les matches 
        matches_1 = [] 
        match_1 = [] 
        match_2 = [] 
        match_3 = [] 
        match_4 = [] 
        for m in range(len(tuples)-6): 
            match_1.append(tuples[m]) 
        for m in range(2, len(tuples)-4): 
            match_2.append(tuples[m]) 
        for m in range(4, len(tuples)-2): 
            match_3.append(tuples[m]) 
        for m in range(6, len(tuples)): 
            match_4.append(tuples[m]) 
        matches_1.append(match_1) 
        matches_1.append(match_2) 
        matches_1.append(match_3) 
        matches_1.append(match_4) 
        print(f'match_1 : {match_1}') 
        print(f'match_2 : {match_2}') 
        print(f'matches_1 : {matches_1}') 

        return matches_1 
    
    



