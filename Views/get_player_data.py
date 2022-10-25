



from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 
import re 
# from .Controllers.players_controller import Try_controller     # essayer d'atteindre le controleur  



class Player_prompt_view(): 

#     prnt = Try_controller() 
#     # pass 

    def prompt_for_player_data(): 
        """ Get the player data via prompt inputs in the console. 
            The player_controller gets the data and send it to the player_model, 
            that formates them in order to send them to the DB. 
        """ 

        # List for the players data  
        # players_data = [] 

        # Prompts for tournament configuration 
        # ask_for_current_year = int(session.prompt('What\'s the current year ?\n')) 
        # ask_for_min_age = int(session.prompt('What is the min. age ?\n')) 

        # ask_for_number_of_players = session.prompt('How many players left ? \n') 
        # players_to_register = int(ask_for_number_of_players) 
        # print('\nplayers_to_register (ln20) : ', players_to_register) 

        # while players_to_register > 0: 

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
        # players_data.append(player_data) 

        # players_to_register -= 1 
        # print('\nplayers_to_register (ln64) : ', players_to_register) 


        # formated_player_data = formate_data(player_data) 

        return player_data 


    def formate_data(player_data): 

        formated_player_data = {} 

        # formate data 
        formated_player_data['lastname'] = player_data['lastname'].capitalize() 
        formated_player_data['firstname'] = player_data['firstname'].capitalize() 

        # formate birthdate 
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
            formated_player_data['genre'] = player_data['genre'] 
        else: 
            formated_player_data['genre'] = session.prompt(
                'Unknown letter. Enter the player genre: M, F, O (for "other") in capitals: \n'
            ) 
        
        formated_player_data['classement'] = player_data['classement'] 


        return formated_player_data 



    # def formate_data(players_data): 

    #     formated_players_data = {} 

    #     # formate data 
    #     formated_players_data['lastname'] = int(players_data['ask_for_lastname']).capitalize() 
    #     formated_players_data['firstname'] = int(players_data['ask_for_firstname']).capitalize() 

    #     # lastname = ask_for_lastname.capitalize() 
    #     # firstname = ask_for_firstname.capitalize() 

    #     # annee_en_cours = ask_for_current_year 
    #     # age_mini = ask_for_min_age 

    #     # formate birthdate 
    #     if re.search('\d\d\d\d[-\d\d]+', players_data['ask_for_birthdate']): 
    #         # print(re.search('\d\d\d\d[-\d\d]+', ask_for_birthdate)) 
    #         formated_players_data['birthdate'] = players_data['ask_for_birthdate'] 
    #         print(f'birthdate : {formated_players_data["birthdate"]}') 
    #     else: 
    #         formated_players_data['birthdate'] = session.prompt('Enter the player birthdate (YYYY-MM-DD): \n') 
    #         print(f'ask_for_birthdate : {formated_players_data["birthdate"]}') 

    #     # formate genre 
    #     if (players_data['ask_for_genre'] == 'M') | (players_data['ask_for_genre'] == 'F') | (players_data['ask_for_genre'] == 'O'): 
    #         formated_players_data['genre'] = players_data['ask_for_genre'] 
    #     else: 
    #         formated_players_data['genre'] = session.prompt(
    #             'Unknown letter. Enter the player genre: M, F, O (for "other") in capitals: \n'
    #         ) 
        
    #     formated_players_data['classement'] = players_data['ask_for_classement'] 


    #     return formated_players_data 




