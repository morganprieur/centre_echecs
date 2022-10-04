# tu use prompt as an instance 
from prompt_toolkit import PromptSession 
session = PromptSession() 

# Doctest 
def to_absolute(number): 
    """
    >>> to_absolute(3)
    3
    >>> to_absolute(-4)
    4
    """
    if number < 0: 
        return -number 
    else: 
        return number 



# Prompt to ask the attributes of one player 
def prompt_for_one_player(): 
    # print(f'Lastname : {ask_for_lastname}') 
    # print(f'Firstname : {ask_for_firstname}') 
    # print(f'Birthdate : {ask_for_birthdate}') 
    # print(f'Genre : {ask_for_genre}') 
    # print(f'Classement : {ask_for_classement}') 
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
        ), 
        'ask_for_new_player': session.prompt(
            'Do you want to register another new player ? (Y maj / N maj) \n'
        ) 
    } 


    # Condition if another new player or not 
    if player_data['ask_for_new_player'] == 'Y': 
        # other_player = prompt_for_one_player() 
        print('another player') 
    elif player_data['ask_for_new_player'] == 'N': 
        print('done') 
    else: 
        print('Unknown command') 


    return player_data 



def serialize_player(lastname, firstname, birthdate, genre, classement): 
    serialize_player_data = {
        'lastname': lastname, 
        'firstname': firstname, 
        'birthdate': birthdate, 
        'genre': genre, 
        'classement': classement 
    }

    return serialize_player_data 


