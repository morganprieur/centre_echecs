



# test 
from test.player_test import Set_player_data 

from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 

import re 


class Get_player_view(): 

    def prompt_for_player_data(): 

    # def prompt_for_player_data(): 
        """ Get the player data via prompt inputs in the console. 
            The player_controller gets the data and send it to the player_model, 
            that formates them in order to send them to the DB. 
        """ 

        # Prompts for tournament configuration 
        # ask_for_current_year = int(session.prompt('What\'s the current year ?\n')) 
        # ask_for_min_age = int(session.prompt('What is the min. age ?\n')) 

        # Prompt to ask the attributes of one player 
        ask_for_lastname = session.prompt('Enter the player lastname: \n') 
        ask_for_firstname = session.prompt('Enter the player firstname: \n') 
        ask_for_birthdate = session.prompt('Enter the player birthdate (YYYY-MM-DD): \n') 
        ask_for_genre = session.prompt('Enter the player genre (M, F, O for "other") in capitals: \n') 
        ask_for_classement = int(session.prompt('Enter the player classement: \n')) 


        # Formated data for one player 
        player_data = { 
            'lastname': ask_for_lastname, 
            'firstname': ask_for_firstname, 
            'birthdate': ask_for_birthdate, 
            'genre': ask_for_genre, 
            'classement': ask_for_classement 
        } 

        return player_data 


    def formate_data(player_data): 
        """ Formate data for the current player 

        Args:
            player_data (dictionnary): the raw data, entered by the administrator 

        Returns:
            dictionnary: the formated data for one player 
        """

        formated_player_data = {} 

        # formate data 
        formated_player_data['lastname'] = player_data['lastname'].capitalize() 
        formated_player_data['firstname'] = player_data['firstname'].capitalize() 

        # for formating birthdate 
        # annee_en_cours = ask_for_current_year 
        # age_mini = ask_for_min_age 
        if re.search('\d\d\d\d[-\d\d]+', player_data['birthdate']): 
            # print(re.search('\d\d\d\d[-\d\d]+', ask_for_birthdate)) 
            formated_player_data['birthdate'] = player_data['birthdate'] 
            print(f'birthdate : {formated_player_data["birthdate"]}') 
        else: 
            formated_player_data['birthdate'] = session.prompt('Enter the player birthdate (YYYY-MM-DD): \n') 
            print(f'ask_for_birthdate : {formated_player_data["birthdate"]}') 

        # formate genre 
        # if (player_data['genre'] == 'M') | (player_data['genre'] == 'F') | (player_data['genre'] == 'O'): 
        #     print(f'Unknown letter : {player_data["genre"]}\n') 
        #     formated_player_data['genre'] = player_data['genre'] 
        # else: 
        #     print(f'type of genre : {type(player_data["genre"])}') 
        #     formated_player_data['genre'] = session.prompt( 
        #         f'Unknown letter : {player_data["genre"]}Enter the player genre: M, F, O (for "other") in capitals: \n'
        #     ) 
        formated_player_data['genre'] = player_data['genre'] 
        
        formated_player_data['classement'] = player_data['classement'] 
        print(f'formated_player_data ln V48 : {formated_player_data}') 

        return formated_player_data 


    def get_many_players(): 
        """ Group the current players in one list 

        Returns:
            list: list of the current players, with data verified and formated in order to work with 
        """

        # Players to register 
        ask_for_number_of_players = session.prompt('How many players left ? \n') 

        players_to_register = int(ask_for_number_of_players) 
        print('\nplayers_to_register (ln20) : ', players_to_register) 

        formated_players = [] 

        # Choix test ou pas : 
        test_ou_pas = session.prompt('test ? (Y/N)') 
        if test_ou_pas == 'Y': 
            # test players 
            player_data = Set_player_data.test_players(players_to_register) 

        else: 
            while players_to_register > 0: 
                player_data = Get_player_view.prompt_for_player_data() 


        # player_data = Get_player_view.prompt_for_player_data() 
        formated_player_data = Get_player_view.formate_data(player_data) 

        formated_players.append(formated_player_data) 
        print(f'formated_players ln V95 : {formated_players}') 

        players_to_register -= 1 
        print('\nplayers_to_register (ln91) : ', players_to_register) 
        
        return formated_players 


