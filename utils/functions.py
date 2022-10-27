

# import re 
# # tu use prompt as an instance 
# from prompt_toolkit import PromptSession 
# session = PromptSession() 
# from datetime import datetime, date 




# class Player_manager(): 



#     # test imports 
#     # def try_modules(weather): 
#     #     print(f'the weather is {weather}') 


    



#     # def prompt_for_players_data(): 
#     #     """ Get the players data via prompt inputs in the console. 
#     #         Calls another function in order to formate the data. 
#     #     """ 

#     #     # List for the players data  
#     #     players_data = [] 

#     #     # Prompts for tournament configuration 
#     #     # ask_for_current_year = int(session.prompt('What\'s the current year ?\n')) 
#     #     # ask_for_min_age = int(session.prompt('What is the min. age ?\n')) 

#     #     ask_for_number_of_players = session.prompt('How many players left ? \n') 
#     #     players_to_register = int(ask_for_number_of_players) 
#     #     print('\nplayers_to_register (ln20) : ', players_to_register) 

#     #     while players_to_register > 0: 

#     #         # Prompt to ask the attributes of one player 
#     #         ask_for_lastname = session.prompt('Enter the player lastname: \n') 
#     #         ask_for_firstname = session.prompt('Enter the player firstname: \n') 
#     #         ask_for_birthdate = session.prompt('Enter the player birthdate (YYYY-MM-DD): \n') 
#     #         # ask_for_birth_month = session.prompt('Enter the player birth month (MM): \n') 
#     #         # ask_for_birth_year = session.prompt('Enter the player birth year (YYYY): \n') 
#     #         ask_for_genre = session.prompt('Enter the player genre (M, F, O for "other") in capitals: \n') 
#     #         ask_for_classement = int(session.prompt('Enter the player classement: \n')) 





#             # # formate data 
#             # lastname = ask_for_lastname.capitalize() 
#             # firstname = ask_for_firstname.capitalize() 

#             # # annee_en_cours = ask_for_current_year 
#             # # age_mini = ask_for_min_age 

#             # # formate birthdate 
#             # if re.search('\d\d\d\d[-\d\d]+', ask_for_birthdate): 
#             #     # print(re.search('\d\d\d\d[-\d\d]+', ask_for_birthdate)) 
#             #     birthdate = ask_for_birthdate 
#             #     print(f'birthdate : {birthdate}') 
#             # else: 
#             #     ask_for_birthdate = session.prompt('Enter the player birthdate (YYYY-MM-DD): \n') 
#             #     # print(f'ask_for_birthdate : {ask_for_birthdate}') 

#             # # formate genre 
#             # if (ask_for_genre == 'M') | (ask_for_genre == 'F') | (ask_for_genre == 'O'): 
#             #     genre = ask_for_genre 
#             # else: 
#             #     genre = session.prompt(
#             #         'Unknown letter. Enter the player genre: M, F, O (for "other") in capitals: \n'
#             #     ) 
            
#             # classement = ask_for_classement 


#         #     # Formated data for one player 
#         #     player_data = { 
#         #         'lastname': lastname, 
#         #         'firstname': firstname, 
#         #         'birthdate': birthdate, 
#         #         'genre': genre, 
#         #         'classement': classement 
#         #     } 


#         #     players_data.append(player_data) 
#         #     players_to_register -= 1 
#         #     print('\nplayers_to_register (ln83) : ', players_to_register) 

#         # return players_data 


#     # # ref circ... ? 
#     # def formate_data(players_data): 

#     #         # formate data 
#     #     lastname = ask_for_lastname.capitalize() 
#     #     firstname = ask_for_firstname.capitalize() 

#     #     # annee_en_cours = ask_for_current_year 
#     #     # age_mini = ask_for_min_age 

#     #     # formate birthdate 
#     #     if re.search('\d\d\d\d[-\d\d]+', ask_for_birthdate): 
#     #         # print(re.search('\d\d\d\d[-\d\d]+', ask_for_birthdate)) 
#     #         birthdate = ask_for_birthdate 
#     #         print(f'birthdate : {birthdate}') 
#     #     else: 
#     #         ask_for_birthdate = session.prompt('Enter the player birthdate (YYYY-MM-DD): \n') 
#     #         # print(f'ask_for_birthdate : {ask_for_birthdate}') 

#     #     # formate genre 
#     #     if (ask_for_genre == 'M') | (ask_for_genre == 'F') | (ask_for_genre == 'O'): 
#     #         genre = ask_for_genre 
#     #     else: 
#     #         genre = session.prompt(
#     #             'Unknown letter. Enter the player genre: M, F, O (for "other") in capitals: \n'
#     #         ) 
        
#     #     classement = ask_for_classement 


    

#         """ 
#             # def formate_birthdate(time): 
#             #     if time == 'day': 
#             #         time_str = 'day (DD)' 
#             #     elif time == 'month': 
#             #         time_str = 'month (MM)' 
#             #     elif time == 'year': 
#             #         time_str = 'year (YYYY)' 

#             #     flag = False 
#             #     while not flag: 
#             #         timelaps = session.prompt(f'Enter the player birth {time_str}: \n') 
#             #         if time == 'day': 
#             #             flag_str = (int(timelaps) >= int('01')) & (int(timelaps) <= (int('31'))) 
#             #             day = timelaps 
#             #         elif time == 'month': 
#             #             flag_str = (int(timelaps) >= int('01')) & (int(timelaps) <= (int('12'))) 
#             #             month = timelaps 
#             #         elif time == 'year': 
#             #             flag_str = (int(timelaps) > 1000) & (int(timelaps) <= (int(annee_en_cours) - age_mini)) 
#             #             year = timelaps 
#             #         print(flag) 
#             #         flag = flag_str 
#             #         print(f'{time} : ', timelaps) 
#             #         if timelaps == 'exit': 
#             #             flag = True 
#             #         print(flag) 
#             #     return timelaps 
#             # # à tester : 
#             # formate_birthdate('day') 
#             # formate_birthdate('month') 
#             # formate_birthdate('year') 
#             # birthdate = f'{str(year)}-{str(month)}-{str(day)}' 

#             # flag_day = False 
#             # while not flag_day: 
#             #     day = session.prompt('Enter the player birth day (DD): \n') 
#             #     print(flag_day) 
#             #     flag_day = (int(day) >= int('01')) & (int(day) <= (int('31'))) 
#             #     print('day : ', day) 
#             #     if day == 'exit': 
#             #         flag_day = True 
#             #     print(flag_day) 

#             # flag_month = False 
#             # while not flag_month: 
#             #     month = session.prompt('Enter the player birth month (MM): \n') 
#             #     print(flag_month) 
#             #     flag_month = (int(month) >= int('01')) & (int(month) <= (int('12'))) 
#             #     print('month : ', month) 
#             #     if month == 'exit': 
#             #         flag_month = True 
#             #     print(flag_month) 

#             # flag_year = False 
#             # while not flag_year: 
#             #     year = session.prompt('Enter the player birth year (YYYY) ln52: \n') 
#             #     print(flag_year) 
#             #     flag_year = (int(year) > 1000) & (int(year) <= (int(annee_en_cours) - age_mini)) 
#             #     print('year : ', year)  
#             #     if year == 'exit': 
#             #         flag_year = True 
#             #     print(flag_year) 

#             # if 1000 > int(ask_for_birth_year) & int(ask_for_birth_year) < 2016: 
#             #     year = ask_for_birth_year 
#             # else: 
#             #     year = session.prompt(
#             #         'Bad format. Enter the player birth year with 4 digits: \n'
#             #     ) 

#             # if re.search('^\d\d$', ask_for_birth_month) == True: 
#             #     month = ask_for_birth_month 
#             # else: 
#             #     month = re.sub('^\d$', f'0{ask_for_birth_month}', ask_for_birth_month) 

#             # if re.search('^\d\d$', ask_for_birth_day) == True: 
#             #     day = ask_for_birth_day 
#             # else: 
#             #     day = re.sub('^\d$', f'0{ask_for_birth_day}', ask_for_birth_day) 

#             # birthdate = f'{str(year)}-{str(month)}-{str(day)}' 
#         """ 




#     def serialize_one_player(lastname, firstname, birthdate, genre, classement): 
#         """ Serialize one player in order to register it in the DB """ 

#         serialize_player_data = {
#             'lastname': lastname, 
#             'firstname': firstname, 
#             'birthdate': birthdate, 
#             'genre': genre, 
#             'classement': classement 
#         }

#         return serialize_player_data 


#     def serialize_multi_players(players): 
#         serialized_players = [] 

#         for p_obj in range(len(players)): 
#             # print(f'p_obj : {p_obj}\n') 
#             p_serial = serialize_one_player( 
#                 lastname=players[p_obj].lastname, 
#                 firstname=players[p_obj].firstname, 
#                 birthdate=players[p_obj].birthdate, 
#                 genre=players[p_obj].genre, 
#                 classement=players[p_obj].classement
#             ) 
#             # print('p_serial : ', p_serial) 
#             serialized_players.append(p_serial) 

#         return serialized_players 

