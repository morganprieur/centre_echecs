



# from Views.dashboard_view import Dashboard_view 
# from Controllers.players_controller import Register_players  
# from Models.player_model import Player 



import os 
# Dossier du projet 
folder = os.path.dirname(__file__) 
# functions 
# from utils.functions import prompt_for_players_data, serialize_multi_players, try_modules 
# from Controllers.players_controller import Register_players 


# db = TinyDB('db.json') 
# players_table = db.table('players') 


# from . import Classe2
# #ou
# from .Classes import Classe2



# class Trying(): 

#     # pl = Player(firstname='firstname', lastname='lastname', birthdate='2022-10-13', genre='M', classement='45') 
#     # print(pl) 

#     print('trying class') 

#     ojd = try_modules('pluie') 












if __name__ == "__main__": 
#     from utils.functions import prompt_for_players_data, serialize_multi_players 
    from Models.player_model import Player 
    from Controllers.players_controller import Register_players 
    from Views.dashboard_view import Dashboard_view 



