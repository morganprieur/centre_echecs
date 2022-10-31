



# test 
# from test.player_test import Get_player_data 

from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 

import re 


class Get_player_view(): 

    # def prompt_for_player_data(): 
    def prompt_for_player_data(players_to_register): 
        """ Get the player data via prompt inputs in the console. 
            The player_controller gets the data and send it to the player_model, 
            that formates them in order to send them to the DB. 
        """ 

        # Prompts for tournament configuration 
        # ask_for_current_year = int(session.prompt('What\'s the current year ?\n')) 
        # ask_for_min_age = int(session.prompt('What is the min. age ?\n')) 
        
        player_data = {} 

        # Choix test ou pas : 
        test_ou_pas = session.prompt('test ? (Y/N)') 

        if test_ou_pas == 'Y': 
            # player_data = Get_player_data.test_players(players_to_register) 
            # while players_to_register > 0: 
            with open("./utils/players_data.txt", "r") as file: 
                lines = file.readlines() 
                for pl_reg in range(players_to_register): 
                    print(f'type of lines : {type(lines)}') 
                    
                    # for pl_reg in range(players_to_register): 
                    # for line in range(len(lines)%(players_to_register*5)): 
                    # print(f'players_to_register : {players_to_register}') 
                    print(f'pl_reg : {pl_reg}') 
                    # print(f'line : {line}') 
                    # while line < player_datas: 
                    ask_for_lastname = lines[(pl_reg*5)] 
                    print(f'ligne : {pl_reg*5}') 
                    print(f'ask_for_lastname : {ask_for_lastname}') 
                    ask_for_firstname = lines[(pl_reg*5)+1] 
                    print(f'ligne : {(pl_reg*5)+1}') 
                    print(f'ask_for_firstname : {ask_for_firstname}') 
                    ask_for_birthdate = lines[(pl_reg*5)+2] 
                    print(f'ligne : {(pl_reg*5)+2}') 
                    print(f'ask_for_birthdate : {ask_for_birthdate}') 
                    ask_for_genre = lines[(pl_reg*5)+3] 
                    print(f'ligne : {(pl_reg*5)+3}') 
                    print(f'ask_for_genre : {ask_for_genre}') 
                    ask_for_classement = lines[(pl_reg*5)+4] 
                    print(f'ligne : {(pl_reg*5)+4}') 
                    print(f'ask_for_classement : {ask_for_classement}') 
                    # Data for one player 
                    player_data = { 
                        'lastname': ask_for_lastname, 
                        'firstname': ask_for_firstname, 
                        'birthdate': ask_for_birthdate, 
                        'genre': ask_for_genre, 
                        'classement': ask_for_classement 
                    } 
                    print(f'player_data V70 : {player_data}') 

        elif test_ou_pas == 'N': 

            # Prompt to ask the attributes of one player 
            ask_for_lastname = session.prompt('Enter the player lastname: \n') 
            ask_for_firstname = session.prompt('Enter the player firstname: \n') 
            ask_for_birthdate = session.prompt('Enter the player birthdate (YYYY-MM-DD): \n') 
            ask_for_genre = session.prompt('Enter the player genre (M, F, O for "other") in capitals: \n') 
            ask_for_classement = int(session.prompt('Enter the player classement: \n')) 

            # Data for one player 
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
        print(f'formated_player_data ln V48 : {formated_player_data}')  # à l'endroit 

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

        # # Choix test ou pas : 
        # test_ou_pas = session.prompt('test ? (Y/N)') 
        
        # if test_ou_pas=='N': 
        while players_to_register > 0: 
            player_data = Get_player_view.prompt_for_player_data(players_to_register) 

            # player_data = Get_player_view.prompt_for_player_data() 
            formated_player_data = Get_player_view.formate_data(player_data) 

            formated_players.append(formated_player_data) 
            print(f'formated_players ln V95 : {formated_players}')  # inversés 

            players_to_register -= 1 
            print('\nplayers_to_register (ln91) : ', players_to_register) 
        


            formated_player_data = Get_player_view.formate_data(player_data) 

            formated_players.append(formated_player_data) 
            print(f'formated_players ln V95 : {formated_players}')  # inversés 

            players_to_register -= 1 
            print('\nplayers_to_register (ln91) : ', players_to_register) 
        
        return formated_players 


