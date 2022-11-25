




# TinyDB 
from tinydb import TinyDB
db = TinyDB('db.json') 
matches_table = db.table('matches') 



class Match(): 
    """ un match : un tuple de 2 listes -> un ref de joueur + le score pour chacun 
    """ 
    tuple_match = ([], []) 

    matches_obj_start = [] 

    def __init__(self, tuple_match): 
        self.tuple_match = tuple_match 

    def __str__(self): 
        return f'Joueur {self.tuple_match[0][0]} joue contre joueur {self.tuple_match[1][0]}, et le score est de {self.tuple_match[0][1]} à {self.tuple_match[1][1]}' 


    # def instantiate_match(): 

    #     match_y = Match(
    #         tuple_match=([0, 0], [1, 0]) 
    #     ) 

    #     print(match_y) 

    #     return match_y 


    ### ? matches_start vient de Match_controller, comment ça se fait qu'on y accède depuis ce modèle ? 
    def instantiate_matches_start(matches_start, matches_obj_start): 
        # print(f'matches_start MM37 : {matches_start}') 

        # instancier les matches 
        # liste de matches : matches_start 
        # boucler dedans pour instancier chaque match au début 
        for m in range(len(matches_start)): 
            match_y = Match( 
                tuple_match=matches_start[m] 
            ) 
            # print(f'match M45 : {match_y}') 
            matches_obj_start.append(match_y) 
        # print(f'matches_obj_start MM47 : {matches_obj_start}') 

        return matches_obj_start 

    def serialize_multi_matches(matches_obj_start): 
        """ Serialization of the matches data in order to register them 
            in the DB. 
        Args:
            matches (list): list of object Matches_start 
        Returns:
            serialized_matches_start (list): the matches in the expected format for the DB 
        """
        serialized_matches_start = [] 

        # print(f'matches_obj_start M63 : {matches_obj_start}') 
        for m_obj in range(len(matches_obj_start)): 
            # print(f'type(p_obj) : {type(p_obj)}\n') 
            # print(f'p_obj : {p_obj}\n') 
            # print(f'players[{p_obj}] : {players[p_obj]}\n') 
            serialized_match_start_data = {
                'tuple_match': matches_obj_start[m_obj].tuple_match 
            } 

            serialized_matches_start.append(serialized_match_start_data) 

        # print(f'serialized_matches_start M60 : {serialized_matches_start}') 

        matches_table.truncate() 
        # # Enregistrer les joueurs sérialisés dans la bdd : 
        matches_table.insert_multiple(serialized_matches_start) 

        return serialized_matches_start 


    # resultats matches round 1 
    def instantiate_scores_round_1(scores_players_round_1): 
        print(f'scores_round_1 MM40 : {scores_players_round_1}') 

        matches_round_1 = [] 
        # liste de dicts de "adversaire" et "score du joueur" : scores_players_round_1 
        # boucler dedans pour instancier chaque match à la fin du round 1 
        # {'player': 1, 'adversary': '4', 'score': '1'} 
        for m in range(len(scores_players_round_1)): 
            # tuple matches : (player_id, player_score) 
            player_id = scores_players_round_1[m]['player'] 
            player_score = scores_players_round_1[m]['score'] 
            match_round_1 = Match( 
                tuple_match=(player_id, player_score)
            ) 
            matches_round_1.append(match_round_1) 
        print(f'matches_round_1 MM101 : {matches_round_1}') 


        # for m in range(len(matches_start)): 
        #     match_y = Match( 
        #         tuple_match=matches_start[m] 
        #     ) 
        #     # print(f'match M45 : {match_y}') 
        #     matches_obj_start.append(match_y) 
        # # print(f'matches_obj_start MM47 : {matches_obj_start}') 




