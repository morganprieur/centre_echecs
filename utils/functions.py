# tu use prompt as an instance 
from prompt_toolkit import PromptSession 
session = PromptSession() 

# Doctest 
# def to_absolute(number): 
#     """
#     >>> to_absolute(3)
#     3
#     >>> to_absolute(-4)
#     4
#     """
#     if number < 0: 
#         return -number 
#     else: 
#         return number 



# Prompt to ask the attributes of one player 
def prompt_for_players_data(): 
    # print(f'Lastname : {ask_for_lastname}') 
    # print(f'Firstname : {ask_for_firstname}') 
    # print(f'Birthdate : {ask_for_birthdate}') 
    # print(f'Genre : {ask_for_genre}') 
    # print(f'Classement : {ask_for_classement}') 
    players_data = [] 

    ask_for_number_of_players = session.prompt(
        'How many players left ? \n'
    ) 

    nb_players_registered = 0 
    players_to_register = int(ask_for_number_of_players) 

    print('\nplayers_to_register (ln38) : ', players_to_register) 

    while players_to_register > 0: 

        player_data = { 
            'ask_for_lastname': session.prompt(
                'Enter the player lastname: \n'
            ), 
            'ask_for_firstname': session.prompt(
                'Enter the player firstname: \n'
            ), 
            'ask_for_birthdate': session.prompt(
                'Enter the player birthdate: \n'
            ), 
            'ask_for_genre': session.prompt(
                'Enter the player genre: \n'
            ), 
            'ask_for_classement': session.prompt(
                'Enter the player classement: \n'
            ) 
        } 

        players_data.append(player_data) 
        nb_players_registered += 1 
        players_to_register -= 1 

        print('\nnb_players_registered : ',  nb_players_registered) 
        print('\nplayers_to_register (ln66) : ', players_to_register) 
        

    return players_data 


def serialize_player(lastname, firstname, birthdate, genre, classement): 
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
        print(f'p_obj : {p_obj}\n') 
        p_serial = serialize_player( 
            lastname = players[p_obj].lastname, 
            firstname = players[p_obj].firstname, 
            birthdate = players[p_obj].birthdate, 
            genre = players[p_obj].genre, 
            classement = players[p_obj].classement
        ) 
        print('p_serial : ', p_serial) 
        serialized_players.append(p_serial) 

    return serialized_players 

