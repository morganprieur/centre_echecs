# tu use prompt as an instance 
from prompt_toolkit import PromptSession 
session = PromptSession() 
import re 


def prompt_for_players_data(): 
    """ Get the players data via prompt inputs in the console """

    # Liste pour les données des joueurs 
    players_data = [] 

    ask_for_number_of_players = int(session.prompt(
        'How many players left ? \n'
    )) 

    # nb_players_registered = 0 
    players_to_register = int(ask_for_number_of_players) 

    print('\nplayers_to_register (ln38) : ', players_to_register) 

    while players_to_register > 0: 

        # Prompt to ask the attributes of one player 
        ask_for_lastname = session.prompt(
            'Enter the player lastname: \n'
        ) 
        ask_for_firstname = session.prompt(
            'Enter the player firstname: \n'
        ) 
        ask_for_birth_year = session.prompt(
            'Enter the player birth year (YYYY): \n'
        ) 
        ask_for_birth_month = session.prompt(
            'Enter the player birth month (MM): \n'
        ) 
        ask_for_birth_day = session.prompt(
            'Enter the player birth day (DD): \n'
        ) 
        ask_for_genre = session.prompt(
            'Enter the player genre (M, F, O for "other") in capitals: \n'
        ) 
        ask_for_classement = int(session.prompt(
            'Enter the player classement: \n'
        )) 

        # formate data 
        lastname = ask_for_lastname.capitalize() 
        firstname = ask_for_firstname.capitalize() 
        x_year = re.search('^\d\d\d\d$', ask_for_birth_year) 
        print(x_year) 
        if x_year:  # ask_for_birth_year == 
            year = ask_for_birth_year 
            print(ask_for_birth_year) 
        else: 
            print(ask_for_birth_year) 
            year = session.prompt(
                'Bad format. Enter the player birth year with 4 digits: \n'
            ) 

        if re.search('^\d\d$', ask_for_birth_month) == True: 
            month = ask_for_birth_month 
            print(ask_for_birth_month) 
        else: 
            print(ask_for_birth_month) 
            month = re.sub('^\d$', f'0{ask_for_birth_month}', ask_for_birth_month) 

        if re.search('^\d\d$', ask_for_birth_day) == True: 
            day = ask_for_birth_day 
            print(ask_for_birth_day) 
        else: 
            print(ask_for_birth_day) 
            day = re.sub('^\d$', f'0{ask_for_birth_day}', ask_for_birth_day) 
        
        birthdate = f'{str(year)}-{str(month)}-{str(day)}' 

        if (ask_for_genre == 'M') | (ask_for_genre == 'F') | (ask_for_genre == 'O'): 
            genre = ask_for_genre 
        else: 
            genre = session.prompt(
                'Unknown letter. Enter the player genre: M, F, O (for "other") in capitals: \n'
            ) 

        classement = ask_for_classement 

        player_data = { 
            'lastname': lastname, 
            'firstname': firstname, 
            'birthdate': birthdate, 
            'genre': genre, 
            'classement': classement 
        } 

        print('player_data : ', player_data) 

        players_data.append(player_data) 
        # nb_players_registered += 1 
        players_to_register -= 1 
        print('\nplayers_to_register (ln66) : ', players_to_register) 
        # print('\nnb_players_registered : ',  nb_players_registered) 

    return players_data 


def serialize_one_player(lastname, firstname, birthdate, genre, classement): 
    """ Serializer one player in order to register it in the DB """ 

    serialize_player_data = {
        'lastname': lastname, 
        'firstname': firstname, 
        'birthdate': birthdate, 
        'genre': genre, 
        'classement': classement 
    }

    return serialize_player_data 


def serialize_multi_players(players): 
    serialized_players = [] 

    for p_obj in range(len(players)): 
        # print(f'p_obj : {p_obj}\n') 
        p_serial = serialize_one_player( 
            lastname = players[p_obj].lastname, 
            firstname = players[p_obj].firstname, 
            birthdate = players[p_obj].birthdate, 
            genre = players[p_obj].genre, 
            classement = players[p_obj].classement
        ) 
        # print('p_serial : ', p_serial) 
        serialized_players.append(p_serial) 

    return serialized_players 

