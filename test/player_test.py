



class Get_player_data(): 

    # def test_players(players_to_register): 
    def test_players(players_to_register): 

        while players_to_register > 0: 
            for pl_reg in range(players_to_register): 
                with open("./utils/players_data.txt", "r") as file: 
                    lines = file.readlines() 
                    print(f'type of lines : {type(lines)}') 
                    
                    # datas = players_to_register*5 
                    # player_data_lines = 5  
                    # print(f'data_sets : {data_sets}') 

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

            formated_player_data = Get_player_view.formate_data(player_data) 

             formated_players.append(formated_player_data) 
            print(f'formated_players ln V95 : {formated_players}')  # inversés 

            players_to_register -= 1 
            print('\nplayers_to_register (ln91) : ', players_to_register) 

                
                # while line < datas: 
                #     ask_for_lastname = lines[0] 
                #     print(f'ask_for_lastname : {ask_for_lastname}') 
                #     ask_for_firstname = lines[1] 
                #     print(f'ask_for_firstname : {ask_for_firstname}') 
                #     ask_for_birthdate = lines[2] 
                #     print(f'ask_for_birthdate : {ask_for_birthdate}') 
                #     ask_for_genre = lines[3] 
                #     print(f'ask_for_genre : {ask_for_genre}') 
                #     ask_for_classement = lines[4] 
                #     print(f'ask_for_classement : {ask_for_classement}') 
                #     # print(players) 
                #     datas = 0 

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




