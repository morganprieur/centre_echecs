



from utils.functions import format_capitalize, format_condition, format_date 

from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 

import re 


### Hypothèse classes mères : ### 


# classe mère 
class Persist_entity(): 

    def instantiate(list_of_entities, list_of_objects): 
        Object = 'object'   # juste pour le warning de l'IDE 
        list_of_objects = [] 
        for l in range(len(list_of_entities)): 
            object = Object(
                properties=list_of_entities[l]   # --> boucler dans la liste des props (possible dans une classe ?) 
            ) 
            list_of_objects.append(object) 
        return list_of_objects 
  

    def serialize_objects(list_of_objects, serialized_objects): 
        """ Serialization of the objects in order to register them in the DB. 
        Args:
            list_of_objects (list): list of object to serialize 
        Returns:
            serialized_objects (list): the objects in the expected format for the DB 
        """ 
        serialized_objects = [] 
        for l in range(len(list_of_objects)): 
            serialized_objects = { 
                'properties': list_of_objects[l].properties   # --> boucler dans la liste des props (possible dans une classe ?) 
            } 
            serialized_objects.append(serialized_objects) 
        return serialized_objects 

    # classes filles 
    # ->  class Player(Persist_entity) 
    # ->  class match(Persist_entity) 
    # ->  ... 




