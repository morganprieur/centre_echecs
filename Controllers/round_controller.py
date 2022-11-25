

from Views.round_view import Round_view 
from Controllers.match_controller import Match_controller 
from Models.match_model import Match 
from Models.round_model import Round 


class Round_controller(): 

    matches_obj_start = Match.matches_obj_start 

    def start_round_1(): 
        print('[round_controller] start round 1') 
        Round_controller.round_1(Round_controller.matches_obj_start) 
        # print(f'matches_obj_start RC15 : {Round_controller.matches_obj_start}') 

        ## round 1 
    def round_1(matches_obj_start): 
        # print(f'matches_obj_start RC19 : {matches_obj_start}') 
        
        # Vérifier les données (dans la vue) 
        # cycle round_1 pour 1 joueur 
        # pour tous les joueurs ensuite 
        score_player_1_round_1 = Round_view.get_scores_round_1( 
            Round_controller.matches_obj_start  
        ) 
        # print(f'score_player_1_round_1 RC25 : {score_player_1_start}') 



        # scores_round_1_obj = 
        Match.instantiate_scores_round_1(Round_view.scores_players_round_1) 



