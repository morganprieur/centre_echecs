



# TinyDB 
from tinydb import TinyDB
db = TinyDB('db.json') 
rounds_table = db.table('rounds') 

from datetime import datetime 


class Round(): 
    """ un round : un nom ("round 1"...), liste de 4 matches, un début (datetime), une fin (datetime) 
    """ 

    round_name = str 
    matches = [] 
    debut = datetime 
    fin = datetime 

    def __init__(self, round_name, matches, debut, fin) -> None:
        round_name = self.round_name 
        matches = self.matches 
        debut = self.debut 
        fin = self.fin 

    def __str__(self): 
        for m in self.matches:
            return f'Tour : {self.round_name}, \nmatches : \n{self.matches[m]}, \ndébut : {self.debut}, fin : \n{self.fin}' 


    def instantiate_round(scores_round_1): 
        # liste de scores 
        # boucler dedans pour peupler les tuples des matches --> dans Match 
        # instancier le round avec les matches juste instanciés 

        round_z = Round( 
            round_name=scores_round_1 
        ) 

    #     print(match_y) 

    #     return match_y 


    def instantiate_matches(matches_start, matches_obj_start): 
        # print(f'matches_start MM37 : {matches_start}') 

        # instancier les matches 
        # matches_obj_start = [] 
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
    def instantiate_scores_round_1(score_player_1_round_1): 
        print(f'scores_round_1 MM40 : {score_player_1_round_1}')  




