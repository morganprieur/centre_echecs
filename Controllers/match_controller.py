


from Models.match_model import Match 

# TinyDB 
from tinydb import TinyDB, Query 
db = TinyDB('db.json') 
players_table = db.table('players') 


class Match_controller(): 

    p_table = players_table.all() 
    half_1 = [] 
    half_2 = [] 
    matches_start = [] 

    # def __init__(self, matches_start, matches_obj_start):  ### ? 
    #     self.matches_start = matches_start 
    #     self.matches_obj_start = matches_obj_start 
    #     self.start() 
    
    # matches
    def start_matches(): 
        print('start matches') 
        p_table_classed = Match_controller.sort_players_by_classement( 
            Match_controller.p_table 
        ) 
        Match_controller.separate_players_in_2_halfs( 
            Match_controller.half_1, 
            Match_controller.half_2, p_table_classed 
        ) 
        Match_controller.associate_players_for_round_1( 
            Match_controller.half_1, 
            Match_controller.half_2, 
            Match_controller.matches_start 
        ) 
        # print(f'matches_start MC38 : Match_controller.{Match_controller.matches_start}') 
        Match.instantiate_matches_start( 
            Match_controller.matches_start, 
            Match.matches_obj_start 
        ) 
        # print(f'matches_obj_start MC42 : {Match.matches_obj_start}') 
        
    
    # Associer les joueurs pour chaque match du tour 1 
    def sort_players_by_classement(p_table):   # Player 
        sort_on = 'classement' 
        decorated = [(dict_[sort_on], dict_) for dict_ in  p_table] 
        decorated.sort() 
        result = [dict_ for (key, dict_) in decorated] 
        # print(f'result MC53 : {result}') 

        return result 


    def separate_players_in_2_halfs(half_1, half_2, p_table_classed): 
        
        # séparer les joueurs en 2 moitiés 
        for i in range(len(p_table_classed)): 
            # print(f'p_table_classed[i].doc_id MC60 : {p_table_classed[i].doc_id}') 
            # print(f'p_table_classed[i] MC61 : {p_table_classed[i]}') 
            if i < len(p_table_classed)/2: 
                # print(i) 
                half_1.append(p_table_classed[i]) 
            if len(p_table_classed)/2 <= i: 
                # print(i) 
                half_2.append(p_table_classed[i]) 
        # print(f'half_1 MC70 : {half_1}') 
        # print(f'half_2 MC71 : {half_2}') 

        return half_1, half_2 


    def associate_players_for_round_1(half_1, half_2, matches_start): 
        # associer chaque rang de chaque moitié 
        # print(f'half_1 MC79 : {half_1}') 
        # print(f'half_2 MC80 : {half_2}') 
        
        # utiliser l'id des joueurs 
        tuples = [] 
        for i in range(len(half_1)): 
            # print(f'half_1[i].doc_id C108 : {half_1[i].doc_id}') 
            tuples.append((half_1[i].doc_id, 0)) 
        for i in range(len(half_2)): 
            # print(f'half_2[i].doc_id C111 : {half_2[i].doc_id}') 
            tuples.append((half_2[i].doc_id, 0)) 
            # eval(f"tuple_{i}") = ({half_1[i].doc_id}, 0) 
        # print(f'tuples MC91 : {tuples}') 
        # print(f'type(tuples) MC92 : {type(tuples)}') 
        # print(f'len(tuples) MC93 : {len(tuples)}') 

        # associer les tuples dans les matches 
        match_1 = [] 
        match_2 = [] 
        match_3 = [] 
        match_4 = [] 
        # créer tuples (player_id, score=0) pour chaque joueur 
        for m in range(len(tuples)-6): 
            match_1.append(tuples[m]) 
        for m in range(2, len(tuples)-4): 
            match_2.append(tuples[m]) 
        for m in range(4, len(tuples)-2): 
            match_3.append(tuples[m]) 
        for m in range(6, len(tuples)): 
            match_4.append(tuples[m]) 
        matches_start.append(match_1) 
        matches_start.append(match_2) 
        matches_start.append(match_3) 
        matches_start.append(match_4) 
        # print(f'match_1 MC112 : {match_1}') 
        # print(f'match_2 MC113 : {match_2}') 
        # print(f'matches_start MC114 : {matches_start}') 

        return matches_start 
    
    