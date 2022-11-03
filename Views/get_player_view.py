



# test 
# from test.player_test import Get_player_data 

from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 

import re 


class Get_player_view(): 

    # def formate_data(player_data): 
    #     pass 

    def get_data_file(players_to_register): 

        # Prompts for tournament configuration 
        # ask_for_current_year = int(session.prompt('What\'s the current year ?\n')) 
        # ask_for_min_age = int(session.prompt('What is the min. age ?\n')) 
        
        formated_players = [] 
        print(f'\nformated_players ln V24 : {formated_players}') 
        formated_player_data = {} 

        while players_to_register > 0: 
            with open("./utils/players_data.txt", "r") as file: 
                lines = file.readlines() 
                # print(f'lines : {lines}') 
                for d in range(players_to_register): 
                    # print(f'd avt : {d}') 
                    start = d*5 
                    # print(f'start avt : {start}') 
                    end = start+5 
                    # print(f'end avt : {end}') 
                    step = 5 
                    for i in range(start, end, step): 
                        x = i 
                        # print(f'x : {x}') 
                        data_sets = lines[x:x+step] 
                        # print(f'data_sets : {data_sets}') 

                        # print(f'ligne : {0}') 
                        ask_for_lastname = data_sets[0] 
                        # print(f'ask_for_lastname : {ask_for_lastname}') 
                        # print(f'ligne : {1}') 
                        ask_for_firstname = data_sets[1] 
                        # print(f'ask_for_firstname : {ask_for_firstname}') 
                        # print(f'ligne : {2}') 
                        ask_for_birthdate = data_sets[2] 
                        # print(f'ask_for_birthdate : {ask_for_birthdate}') 
                        # print(f'ligne : {3}') 
                        ask_for_genre = data_sets[3] 
                        # print(f'ask_for_genre : {ask_for_genre}') 
                        # print(f'ligne : {4}') 
                        ask_for_classement = data_sets[4] 
                        # print(f'ask_for_classement : {ask_for_classement}') 
                    
                        # Data for one player 
                        player_data = { 
                            'lastname': ask_for_lastname, 
                            'firstname': ask_for_firstname, 
                            'birthdate': ask_for_birthdate, 
                            'genre': ask_for_genre, 
                            'classement': ask_for_classement 
                        } 
                        # print(f'player_data V71 : {player_data}') 

                        # formate data for one player 
                        formated_player_data = Get_player_view.formate_data(player_data) 
                        
                        # print(f'formated_players ln V76 : {formated_players}') 
                        formated_players.append(formated_player_data) 
                        # print(f'formated_players ln V78 : {formated_players}') 

                    players_to_register -= 1 
                    print(f'players_to_register (ln91) : {players_to_register}') 

        return formated_players 



    # def prompt_for_player_data(): 
    def prompt_for_player_data(players_to_register): 
        """ Get the player data via prompt inputs in the console. 
            The player_controller gets the data and send it to the player_model, 
            that formates them in order to send them to the DB. 
        """ 
        formated_players = [] 
        while players_to_register > 0: 
            print(f'formated_players V94 : {formated_players}') 
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

            # # formate data for one player 
            formated_player_data = Get_player_view.formate_data(player_data) 
            
            # print(f'formated_players ln V113 : {formated_players}') 
            formated_players.append(formated_player_data) 
            # print(f'formated_players ln V115 : {formated_players}') 

            players_to_register -= 1 
            # print(f'\nplayers_to_register (ln91) : {players_to_register}') 

        return formated_players 


    def formate_data(player_data): 
        """ Formate data for the current player 

        Args:
            player_data (dictionnary): the raw data, entered by the administrator 

        Returns:
            formated_player_data (dictionnary): the formated data for the current player 
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
        if (player_data['genre'] == 'M') | (player_data['genre'] == 'F') | (player_data['genre'] == 'O'): 
            print(f'genre : {player_data["genre"]}\n') 
            formated_player_data['genre'] = player_data['genre'] 
        else: 
            print(f'type of genre : {type(player_data["genre"])}') 
            formated_player_data['genre'] = session.prompt( 
                f'Unknown letter : {player_data["genre"]}Enter the player genre: M, F, O (for "other") in capitals: \n'
            ) 
        formated_player_data['genre'] = player_data['genre'] 
        
        formated_player_data['classement'] = player_data['classement'] 
        print(f'formated_player_data ln V48 : {formated_player_data}')  # à l'endroit 

        return formated_player_data 


    def get_many_players():     # dans le controller ? 
        """ Manages number of players and 'test' or 'not test'. 

        Returns:
            formated_players (list): list of the formated players data, in order to work with them. 
        """ 

        ask_for_number_of_players = session.prompt('How many players left ? \n') 
        players_to_register = int(ask_for_number_of_players) 
        # print(f'players_to_register V178 : {players_to_register}') 

        # Choix test ou pas : 
        test_or_not = session.prompt('test ? (Y/N)') 

        if test_or_not == 'Y': 
            formated_players = Get_player_view.get_data_file(players_to_register) 
        
        elif test_or_not=='N': 
            formated_players = Get_player_view.prompt_for_player_data(players_to_register) 

        return formated_players 


