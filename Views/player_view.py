



from Views.abstract_view_classes import Entity_view 
# from utils.functions import format_capitalize, format_condition, format_date 

from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 

import re 


# class Player_view(Entity_view): 
class Player_view(): 

    ask_for_number_of_players = session.prompt('Combien de joueur à enregistrer ? \n') 
    players_to_register = int(ask_for_number_of_players) 
    print(f'players_to_register V183 : {players_to_register}') 
    # Choix test ou pas : 
    test_or_not = session.prompt('test ? (Y/N) : ') 
    formated_players = [] 
    formated_player_data = {} 



    # def __init__(self, formated_players, formated_player_data):     # test_or_not, players_to_register, 
    def __init__(self, test_or_not, players_to_register, formated_players, formated_player_data): 
        self.test_or_not = test_or_not 
        self.players_to_register = players_to_register 
        self.formated_players = formated_players 
        self.formated_player_data = formated_player_data 

        self.get_players() 




    def get_players(self): 
        if self.test_or_not == 'Y': 
            self.formated_players = self.get_data_file() 
        elif self.test_or_not=='N': 
            self.formated_players = self.prompt_for_player_data(self) 


    def get_data_file(self): 
        """ Get data from text file for testing the treatment of the data : 
            store current player data in dictionary, 
            formate current player data, 
            and group the players formated data in a list of dictionaries. 
        Args:
            players_to_register (int): number of players. Used to stop a while loop. 
        Returns:
            formated_players (list of dictionaries): the players formated data in order to work with them. 
        """
        # Prompts for tournament configuration 
        # ask_for_current_year = int(session.prompt('What\'s the current year ?\n')) 
        # ask_for_min_age = int(session.prompt('What is the min. age ?\n')) 
        
        # formated_players = [] 
        # print(f'\nformated_players V31 : {formated_players}') 
        # formated_player_data = {} 

        while self.players_to_register > 0: 
            with open("./utils/players_data.txt", "r") as file: 
                # for line in file:  # sélectionne le contenu de la ligne, pas son index 
                lines = file.readlines() 
                for d in range(self.players_to_register): 
                    start = d*5 
                    end = start+5 
                    step = 5 
                    for i in range(start, end, step): 
                        x = i 
                        data_sets = lines[x:x+step] 
                        
                        ask_for_lastname = data_sets[0] 
                        ask_for_firstname = data_sets[1] 
                        ask_for_birthdate = data_sets[2] 
                        ask_for_genre = data_sets[3] 
                        ask_for_classement = data_sets[4] 
                        
                        # Data for one player 
                        player_data = { 
                            'lastname': ask_for_lastname, 
                            'firstname': ask_for_firstname, 
                            'birthdate': ask_for_birthdate, 
                            'genre': ask_for_genre, 
                            'classement': ask_for_classement 
                        } 
                        # print(f'player_data V75 : {player_data}') 

                        # formate data for one player 
                        formated_player_data = Player_view.formate_data(self, player_data) 
                        
                        # print(f'formated_players V80 : {formated_players}') 
                        # formated_players.append(formated_player_data.copy()) 
                        self.formated_players.append(formated_player_data) 
                        # print(f'formated_players V82 : {formated_players}') 

                    self.players_to_register -= 1 
                    print(f'players_to_register (ln91) : {self.players_to_register}') 

        return self.formated_players 


    # def prompt_for_player_data(): 
    def prompt_for_player_data(self): 
        """ Get the player data via prompt inputs in the console, 
            store current player data in dictionary, 
            formate current player data, 
            and group the players formated data in a list of dictionaries. 
        Args:
            players_to_register (int): number of players. Used to stop a while loop. 
        Returns:
            formated_players (list of dictionaries): the players formated data in order to work with them. 
        """ 
        # formated_players = [] 
        while self.players_to_register > 0: 
            print(f'formated_players V94 : {self.formated_players}') 
            # Prompt to ask the attributes of one player 
            ask_for_lastname = session.prompt('Entrer le nom de famille du joueur : \n') 
            ask_for_firstname = session.prompt('Entrer le prénom du joueur : \n') 
            ask_for_birthdate = session.prompt('Entrer la date de naissance du joueur (AAAA-MM-JJ): \n') 
            ask_for_genre = session.prompt('Entrer le genre  du joueur (M, F, A pour "autre") en majuscules : \n') 
            ask_for_classement = int(session.prompt('Entrer le classement  du joueur : \n')) 

            # Data for one player 
            player_data = { 
                'lastname': ask_for_lastname, 
                'firstname': ask_for_firstname, 
                'birthdate': ask_for_birthdate, 
                'genre': ask_for_genre, 
                'classement': ask_for_classement 
            } 

            # # formate data for one player 
            self.formated_player_data = Player_view.formate_data(player_data) 
            
            # print(f'formated_players V115 : {formated_players}') 
            self.formated_players.append(self.formated_player_data) 
            # print(f'formated_players V117 : {formated_players}') 

            self.players_to_register -= 1 
            # print(f'players_to_register V120 : {players_to_register}') 

        return self.formated_players 


    def formate_data(self, player_data): 
        """ Verifies and formates data for the current player, 
            and adds them at the end of the formated_players list. 
        Args:
            player_data (dictionnary): the raw data, entered by the administrator 
        Returns:
            formated_player_data (dictionnary): the formated data for the current player 
        """ 
        self.formated_player_data = {} 

        # formate data 
        self.formated_player_data['lastname'] = player_data['lastname'].capitalize() 
        self.formated_player_data['firstname'] = player_data['firstname'].capitalize() 

        # for formating birthdate 
        # annee_en_cours = ask_for_current_year 
        # age_mini = ask_for_min_age 
        if re.search('\d\d\d\d[-\d\d]+', player_data['birthdate']): 
           self. formated_player_data['birthdate'] = player_data['birthdate'] 
        else: 
            self.formated_player_data['birthdate'] = session.prompt('Enter the player birthdate (YYYY-MM-DD): \n') 

        # formate genre     # if statement does not work, returns always "else" 
        if ((player_data['genre'] == str('M\n')) or (player_data['genre'] == 'F\n') or (player_data['genre'] == 'A\n')): 
            # print(f'genre : {player_data["genre"]}\n') 
            self.formated_player_data['genre'] = player_data['genre'] 
        else: 
            # print(f'type of genre : {type(player_data["genre"])}') 
            self.formated_player_data['genre'] = session.prompt( 
                f'Lettre non valide : {player_data["genre"]}Entrer le genre du joueur parmi "M", "F", "A" (pour "autre") en majuscules : \n'
            ) 
        # self.formated_player_data['genre'] = player_data['genre'] 
        
        self.formated_player_data['classement'] = player_data['classement'] 

        return self.formated_player_data 


    # def get_many_players():     # dans le controller ? 
    #     """ Manages number of players and 'test' or 'not test'. 
    #     Returns:
    #         formated_players (list): list of the formated players data in dictionnaries, 
    #             in order to work with them. 
    #     """ 
    #     ask_for_number_of_players = session.prompt('Combien de joueur à enregistrer ? \n') 
    #     players_to_register = int(ask_for_number_of_players) 
    #     print(f'players_to_register V183 : {players_to_register}') 

    #     # Choix test ou pas : 
    #     test_or_not = session.prompt('test ? (Y/N) : ') 

    #     if test_or_not == 'Y': 
    #         formated_players = Get_player_view.get_data_file(players_to_register) 
        
    #     elif test_or_not=='N': 
    #         formated_players = Get_player_view.prompt_for_player_data(players_to_register) 
 
    #     return formated_players 


