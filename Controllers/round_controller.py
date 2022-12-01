

from Views.round_view import Round_view 
from Controllers.match_controller import Match_controller 
from Models.match_model import Match 
from Models.round_model import Round 


class Round_controller(): 

    matches_obj_start = Match.matches_obj_start 
    scores_players_round_1 = Round_view.scores_players_round_1 

    def __init__(self, matches_obj_start, scores_players_round_1): 
        self.matches_obj_start = matches_obj_start 
        self.scores_players_round_1 = scores_players_round_1 

    def start_round_1(self): 
        print('[round_controller] start round 1') 

        Round_view.start_round_1(
            Round_view, 
            Round_view.matches_obj_start, 
            Round_view.scores_players_round_1
        ) 
        Round_controller.round_1(self.scores_players_round_1) 
        # print(f'matches_obj_start RC15 : {Round_controller.matches_obj_start}') 


    ## round 1 
    def round_1(scores_players_round_1): 
        """ Get the scores from the Round_view, 
            throw them to the Round_model, 
            who serialize and register them 
            in the 'rounds' table of the DB. 

        Args:
            matches_obj_start (list of dicts): list of the matches with scores incremented 
        """
        # print(f'matches_obj_start RC19 : {matches_obj_start}') 
        # Les données sont vérifiées dans la vue 
        print(f'scores_players_round_1 RC37 : {scores_players_round_1}') 
         
        # score_player_1_round_1 = Round_view.get_scores_round_1( 
        #     Round_controller.matches_obj_start  
        # ) 
        # print(f'score_player_1_round_1 RC25 : {score_player_1_start}') 



        # scores_round_1_obj = 
        # Match.instantiate_scores_round_1(Round_view.scores_players_round_1) 



