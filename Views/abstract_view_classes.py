


from utils.functions import format_capitalize, format_condition, format_date 

from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 

import re 


### Hypothèse classes mères : ### 

# classe mère 
class Entity_view(): 
    
    def get_data(self, list_of_properties):   # list of object's properties to loop on it 
        """ - Get the data via prompt inputs in the console, 
            - store current entity data in dictionary, 
            - formate current entity data, 
            - and group the entities' formated data in a list of dictionaries. 
        Args:
            players_to_register (int): number of players. Used to stop a while loop. 
        Returns:
            formated_entities (list of dictionaries): the entities' formated data in order to work with them. 
        """ 
        players_to_register = session.prompt('Entrer le nombre de joueurs : \n') 


        formated_entities = [] 
        while players_to_register > 0: 
            # Prompt to ask the data of one entity 
            for l in range(len(list_of_properties)): 
                ask_for_data = session.prompt('Entrer l\'info du joueur : \n')  # boucler dans les variables requises ? 

            # Data for one entity 
            entity_data = { 
                'properties': ask_for_data,     # boucler dans les propriétés de l'objet  
            } 

            # formate data for one entity 
            formated_entity_data = self.formate_data(entity_data)   ### c'est comme ça qu'on l'appelle ??? 
            
            formated_entities.append(formated_entity_data) 

            players_to_register -= 1 

        return formated_entities 
    

    def formate_data(entity_data): 
        """ Verifies and formates data for the current entity, 
            and adds them at the end of the formated_entities list. 
        Args:
            entity_data (dictionnary): the raw data, entered by the administrator 
        Returns:
            formated_entity_data (dictionnary): the formated data for the current entity 
        """ 
        formated_entity_data = {} 

        ###A mettre dans des helpers : 
        entity_data = 'list_of_raw_data'   # only for supp the warning of IDE 
        format_capitalize(formated_entity_data, entity_data, 'prop') 
        # for formating birthdate 
        # annee_en_cours = ask_for_current_year 
        # age_mini = ask_for_min_age 
        format_date(entity_data, '\d\d\d\d[-\d\d]+', 'prop') 
        # formate genre     # 'if statement' does not work, returns always "else" 
        list_of_patterns = ['pattern1', 'pattern2', 'pattern3'] 
        format_condition(formated_entity_data, entity_data, list_of_patterns, 'prop') 
        formated_entity_data['classement'] = entity_data['classement'] 

        return formated_entity_data 


    # classes filles 
    # ->  class get_player(prompt) 
    # ->  class get_match(prompt) 
    # ->  ... 
    



