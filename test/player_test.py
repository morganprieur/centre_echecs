



class Set_player_data(): 

    def test_players(players_to_register): 
        with open("./utils/players_data.txt", "r") as file: 
            lines = file.readlines() 
            print(f'type of lines : {type(lines)}') 
            
            datas = players_to_register*5 
            # data_sets = len(lines) / datas 
            # print(f'data_sets : {data_sets}') 

            
            for line in range(len(lines)): 
                print(f'line : {line}') 
                while line < datas: 
                    ask_for_lastname = lines[0] 
                    print(f'ask_for_lastname : {ask_for_lastname}') 
                    ask_for_firstname = lines[1] 
                    print(f'ask_for_firstname : {ask_for_firstname}') 
                    ask_for_birthdate = lines[2] 
                    print(f'ask_for_birthdate : {ask_for_birthdate}') 
                    ask_for_genre = lines[3] 
                    print(f'ask_for_genre : {ask_for_genre}') 
                    ask_for_classement = lines[4] 
                    print(f'ask_for_classement : {ask_for_classement}') 
                    # print(players) 
                    datas = 0 

        # Formated data for one player 
        player_data = { 
            'lastname': ask_for_lastname, 
            'firstname': ask_for_firstname, 
            'birthdate': ask_for_birthdate, 
            'genre': ask_for_genre, 
            'classement': ask_for_classement 
        } 

        return player_data 


# # Test 
# ask_for_test_file = session.prompt('chemin vers le fichier :') 
# print (file.read()) 




