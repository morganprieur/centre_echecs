
class Player(): 
    
    def __init__(self, lastname, firstname, birthdate, genre, classement): 
        self.lastname = lastname  
        self.firstname = firstname 
        self.birthdate = birthdate 
        self.genre = genre 
        self.classement = classement 


    def __str__(self): 
        if self.genre == 'garçon': 
            born = 'né'
        elif self.genre == 'fille': 
            born = 'née' 
        return f'{self.firstname} {self.lastname}' 

    # Pas besoin de méthode spécifique pour ajouter un joueur, on les ajoute manuellement depuis la console 


    

