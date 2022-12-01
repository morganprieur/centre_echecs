



from Models.match_model import Match 
from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 

import re 

class Round_view(): 

    scores_players_round_1 = [] 
    matches_obj_start = Match.matches_obj_start 
    # print(f'matches_obj_start RV15 : {Match.matches_obj_start}')  # liste vide 
    
    def __init__(self, scores_players_round_1, matches_obj_start):
        self.scores_players_round_1 = scores_players_round_1 
        self.matches_obj_start = matches_obj_start 
    

    def start_round_1(self, matches_obj_start, scores_players_round_1): 
        Round_view.get_scores_round_1( 
            matches_obj_start, 
            scores_players_round_1 
        ) 
        # Round_view.get_score_one_player_round_1(self.matches_obj_start) 
        # Round_view.get_scores_round_1(
        #     self.scores_players_round_1, 
        #     self.matches_obj_start 
        # )
    
    """ Exemple création d'un objet, doc drf 
    from datetime import datetime

    class Comment:
        def __init__(self, email, content, created=None):
            self.email = email
            self.content = content
            self.created = created or datetime.now()

    comment = Comment(email='leila@example.com', content='foo bar')
    """

    # cycle round_1 pour 1 joueur 
    def get_score_one_player_round_1(matches_obj_start):  # , id_ 
        score_player_1_round_1 = {} 


        # ask for each player's score 
        ask_for_player_s_score_round_1 = session.prompt(
            # f'Entrer le score du joueur {id_} pour le round 1 : \n' 
            f'Entrer le score du joueur 1 pour le round 1 : \n' 
        ) 
        # score_player_1_round_1['player'] = id_ 
        score_player_1_round_1['player'] = 1 
        score_player_1_round_1['score'] = ask_for_player_s_score_round_1 

        print(f'score_player_round_1 RV40 : {score_player_1_round_1}') 
        print(f'type(score_player_1_round_1) RV64 : {type(score_player_1_round_1)}') 

        # add the current scores in the players table data 
        # get the match_table data (temporary table) 
        # store the rounds' scores in the list of matches for the current round 

        return score_player_1_round_1 
        
    # ensuite pour tous les joueurs
    def get_scores_round_1(matches_obj_start, scores_players_round_1):  # matches_obj_1 
        # créer des dicts pour stocker les joueurs, leur score et les joueurs contre qui ils ont déjà joué 
        # créer une liste pour stocker les dicts 
        # récupérer les scores des joueurs (input) 
        # les enregistrer dans les tuples 
        print(f'self RV75 : {matches_obj_start}') 
        print(f'self RV76 : {scores_players_round_1}') 

        # for i in range(8): 
        #     id_ = i 
        score_player_1_round_1 = Round_view.get_score_one_player_round_1(
            matches_obj_start 
            # , id_ 
        ) 


        # scores_round_1 = [] 
        # player_1_round_1 = {} 
        # player_2_round_1 = {} 
        # player_3_round_1 = {} 
        # player_4_round_1 = {} 
        # player_5_round_1 = {} 
        # player_6_round_1 = {} 
        # player_7_round_1 = {} 
        # player_8_round_1 = {} 

        # scores_round_1.append(player_1_round_1) 
        # scores_round_1.append(player_2_round_1) 
        # scores_round_1.append(player_3_round_1) 
        # scores_round_1.append(player_4_round_1) 
        # scores_round_1.append(player_5_round_1) 
        # scores_round_1.append(player_6_round_1) 
        # scores_round_1.append(player_7_round_1) 
        # scores_round_1.append(player_8_round_1) 

        # Récupérer et traiter les données du joueur 1 : 
        # players_round_1 = [] 
        # score_player_1_round_1 = {} 
        # ask for player's end of match 
        # ask_for_player_s_id = session.prompt(
        #     'Entrer l\'id du joueur : \n' 
        # ) 
        scores_players_round_1.append(score_player_1_round_1) 
        print(f'scores_players_round_1 RV95 : {scores_players_round_1}') 

        return scores_players_round_1 

        # Vérifier les données 





    # Trier tous les joueurs en fonction de leur nombre total de points --> Player.doc_id.nb_points 
    # Si plusieurs joueurs ont le même nombre de points, les trier en fonction de leur rang --> Player.doc_id.classement 
    
    # Associer le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. 
    # Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.





