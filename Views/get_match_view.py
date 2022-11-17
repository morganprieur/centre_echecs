


from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 

import re 

class Get_match_view(): 

    
    def register_scores_round_1(matches_obj_1): 
        # créer des dicts pour stocker les joueurs, leur score et les joueurs contre qui ils ont déjà joué 
        # créer une liste pour stocker les dicts 
        # récupérer les scores des joueurs (input) 
        # les enregistrer dans les tuples 

        # print(f'matches_obj_1 V19 : {matches_obj_1}') 

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

        player_1_round_1 = {} 
        # ask for player's end of match 
        # ask_for_player_s_id = session.prompt(
        #     'Entrer l\'id du joueur : \n' 
        # ) 
        ask_for_player_s_adversary = session.prompt(
            'Entrer l\'id de son adersaire : \n' 
        ) 
        ask_for_player_s_score_round_1 = session.prompt(
            'Entrer le score du joueur pour le round 1 : \n' 
        ) 
        player_1_round_1['adversary'] = ask_for_player_s_adversary 
        player_1_round_1['score'] = ask_for_player_s_score_round_1 


        # if ask_for_player_s_id == 1: 
        #     player_1_round_1['adversary'] = ask_for_player_s_adversary 
        #     player_1_round_1['score'] = ask_for_player_s_score_round_1 
        print(f'player_1_round_1 V58 : {player_1_round_1}')  

        return player_1_round_1 





    # Trier tous les joueurs en fonction de leur nombre total de points --> Player.doc_id.nb_points 
    # Si plusieurs joueurs ont le même nombre de points, les trier en fonction de leur rang --> Player.doc_id.classement 
    
    # Associer le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. 
    # Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.





