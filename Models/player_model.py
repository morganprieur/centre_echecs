



# TinyDB 
# from tinydb import TinyDB
# db = TinyDB('db.json') 
# players_table = db.table('players') 



class Player(): 

    def __init__(self, lastname, firstname, birthdate, genre, classement): 
        self.lastname = lastname  
        self.firstname = firstname 
        self.birthdate = birthdate 
        self.genre = genre 
        self.classement = classement 


    def __str__(self): 
        born = '' 
        if self.genre == 'M': 
            born = 'né'
        elif self.genre == 'F': 
            born = 'née' 
        elif self.genre == 'O': 
            born = 'né.e' 
        return f'{self.firstname} {self.lastname} {born} on {self.birthdate}, place: {self.classement}.' 




