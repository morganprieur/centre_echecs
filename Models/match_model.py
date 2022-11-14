

class Match(): 
    """ un match : un tuple de 2 listes -> un ref de joueur + le score pour chacun 
    """ 
    tuple_match = ([], []) 

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


    def instantiate_matches(matches): 
        # instancier les matches 
        matches_obj = [] 
        for m in range(len(matches)): 
            match_y = Match( 
                tuple_match=matches[m] 
            ) 
            # print(f'match M33 : {match_y}')     
            matches_obj.append(match_y) 
        print(f'matches_obj M35 : {matches_obj}')  


