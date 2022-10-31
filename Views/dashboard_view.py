

from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 

# Affichage Bienvenue + menu + touches de sortie : 
# 0 : menu principal 
# * : menu précédent 

# Afficher le menu 
#   1 : saisies 
#   2 : affichages
# 

# Menu saisir : 
#   1 : un ou des joueurs 
#   2 : un ou des matches 
#   3 : un ou des tours 
#   4 : un ou (?) des tournois 
#   0 : retour au menu précédent


# Menu afficher : 
#   1 : tous les joueurs par ordre alphabétique 
#   2 : tous les joueurs par classement 

#   3 : les joueurs du tournoi par ordre alphabétique 
#   4 : les joueurs du tournoi par classement 

#   5 : les résultats du tournoi 
#   6 : les tours 
#   7 : les matches

#   0 : retour au menu précédent


# # A chaque niveau : 
# # Retour au niveau supérieur 
# # Retour au menu principal 



class Dashboard_view(): 

    welcome_message = [ 
        "\n * * * * * * * * * * * * * * * * "
        "\nBonjour et bienvenue !", 
        "\nCe programme va vous permettre de créer, gérer et afficher vos tournois d\'échecs.", 
        "\nSi vous rencontrez des erreurs, le fichier README.md contient les informations de feedback.", 
        '\nDans le menu, vous pouvez à tout moment utiliser les "commandes de sortie" : ', 
        " * pour revenir au menu précédent,", " 0 pour revenir au menu principal" 
    ] 

    liste_menu_principal = [ 
        "\nMenu principal : ", 
        "1 : Saisir", 
        "2 : Afficher" 
    ] 

    liste_menu_saisir = [
        "Saisir", 
        "1 : un ou des joueurs", 
        "2 : un ou des matches", 
        "3 : un ou des tours", 
        "4 : un ou (?) des tournois", 
        "* : retour au menu précédent", 
        "0 : retour au menu principal" 
    ] 

    liste_menu_afficher = [ 
        "Afficher", 
        "1 : tous les joueurs par ordre alphabétique", 
        "2 : tous les joueurs par classement", 
        "3 : les joueurs du tournoi par ordre alphabétique", 
        "4 : les joueurs du tournoi par classement", 
        "5 : les résultats du tournoi", 
        "6 : les tours", 
        "7 : les matches", 
        "* : retour au menu précédent", 
        "0 retour au menu principal" 
    ] 

    def welcome_view(self): 
        
        for welcome in self.welcome_message: 
            print(welcome) 

        print('') 
        for menu_principal in self.liste_menu_principal: 
            print(menu_principal) 

        # Prompt to ask the action to do 
        ask_for_menu_action = session.prompt('\nChoisir une action : ') 
        # return ask_for_menu_action 

    # def afficher_menu_action(menu_action=welcome_view): 

        # menu_action = Dashboard_view.welcome_view() 
        if ask_for_menu_action == '1': 
            print(f'--> {self.liste_menu_saisir[0]}') 
            
            print('') 
            # menu_saisir = 1 
            for menu_saisir in range(len(self.liste_menu_saisir)): 
                if menu_saisir == 0: 
                    pass 
                else: 
                    print(self.liste_menu_saisir[menu_saisir]) 

            # if "Saisir", prompt to ask the information to enter 
            ask_for_data_to_enter = session.prompt( 
                '\nChoisir quelles données enregistrer : '
            ) 
            data_to_enter = ask_for_data_to_enter 
            print(f'\n{self.liste_menu_saisir[int(data_to_enter)]}') 
        
        elif ask_for_menu_action == '2': 

            for menu_afficher in self.liste_menu_afficher: 
                print(menu_afficher) 

            # if "Afficher", prompt to ask the information to display 
            ask_for_data_to_display = session.prompt( 
                '\nChoisir quelles données afficher : '
            ) 
            data_to_display = ask_for_data_to_display 
            print(f'\n{self.liste_menu_afficher[int(data_to_display)]}') 

        elif ask_for_menu_action == '0': 
            print('\nMerci de choisir "1" pour saisir des informations, ou "2" pour afficher des informations.') 
            Dashboard_view.welcome_view(self) 

        else: 
            print('else') 
            # Dashboard_view.welcome_view() 





    # pass 





