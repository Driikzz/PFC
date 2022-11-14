from random import randint
pseudoJou = input("Choisi ton pseudo : ")
nombreDeManche = int(input("Tu veux jouer combien de manches: "))

import os
clear = lambda: os.system('cls')


def menu(): 
    print(" ")
    print("Bienvenue "+ pseudoJou +" dans le pierre PFC si tu souhaites lancer la partie écris JOUER: ")
    choixMenu = input("Ton choix :")
    if choixMenu == "JOUER" :
        clear()
        game()
    else:
        print("Tampis à bientôt "+ pseudoJou)

def joueur():
    pseudoJoueur = pseudoJou
    choixJoueur = (input((pseudoJoueur +" Tu choisie quelle objets ")))
    pierre = 0
    ciseau = 0
    feuille = 0
    if choixJoueur == "pierre":
        pierre = 1 
        if pierre == 1:
            print(" ")
            print(pseudoJoueur +" à choisi Pierre")
    elif choixJoueur == "ciseaux" : 
        ciseau = 1 
        if ciseau == 1:
            print(" ")
            print(pseudoJoueur +" à choisi Ciseaux")
    elif choixJoueur == "feuille": 
        feuille = 1 
        if feuille == 1:
            print(" ")
            print(pseudoJoueur +" à choisi feuille")

    elif choixJoueur != "pierre" or choixJoueur != "feuille" or choixJoueur != "ciseaux" :
        print("Erreur : Tu n'as pas choisi la bonne valeur")
        choixJoueur = input((pseudoJoueur +" Tu choisie quelle objets "))
    return choixJoueur
    

def bot():
    tableau = ["pierre","feuille","ciseaux"]
    choixBot = tableau[randint(0,2)]
    pierre = 0
    ciseau = 0
    feuille = 0
    
    if choixBot == "pierre": 
        pierre = 1 
        if pierre == 1:
            print(" ")
            print("BOT à choisi Pierre")
    elif choixBot == "feuille" : 
        feuille = 1 
        if feuille == 1:
            print(" ")
            print("BOT à choisi feuille")
    elif choixBot == "ciseaux": 
        ciseau= 1 
        if ciseau ==1:
            print(" ")
            print("BOT à choisi ciseaux")
    return choixBot

def game():
    pointJoueur = 0 
    pointBot = 0   
    while nombreDeManche > pointJoueur or pointBot :
        
        if nombreDeManche == pointJoueur:
            print(" ")
            print("Le gagnant est " + pseudoJou)
        elif nombreDeManche == pointBot :
            print(" ")
            print("Le gagnant est BOT")

        if nombreDeManche == pointJoueur or nombreDeManche == pointBot:
            print(" ")
            print("Fin Tu veux rejouer")
            relancer = input("Ecris oui : ")
            if relancer == "oui":
                clear() 
                game()
            else:
                print("Merci d'avoir jouer "+pseudoJou)
                break
        
        choixJoueurGame = joueur()
        choixBotGame = bot()

        if choixJoueurGame == choixBotGame: 
            print(" ")
            print("Egalité")
            print(" ")
            print("Score :")
            print("Le Bot à :",pointBot)
            print(pseudoJou+" à :",pointJoueur)
            print(" ")

        elif choixJoueurGame == "pierre" and choixBotGame == "feuille" :
            print(" ") 
            print("Le Bot à gagné")
            pointBot = pointBot + 1
            print(" ")
            print("Score :")
            print("Le Bot à :",pointBot)
            print(pseudoJou+" à :",pointJoueur)
            print(" ")
            

        elif choixJoueurGame == "pierre" and choixBotGame == "ciseaux" :
            print(" ") 
            print("Le Joueur à gagné")
            pointJoueur = pointJoueur + 1
            print(" ")
            print("Score :")
            print("Le Bot à :",pointBot)
            print(pseudoJou+" à :",pointJoueur)
            print(" ")
        
        elif choixJoueurGame == "feuille" and choixBotGame == "pierre" :
            print(" ") 
            print("Le Joueur à gagné")
            pointJoueur = pointJoueur +1
            print(" ")
            print("Score :")
            print("Le Bot à :",pointBot)
            print(pseudoJou+" à :",pointJoueur)
            print(" ")

        elif choixJoueurGame == "feuille" and choixBotGame == "ciseaux" :
            print(" ")
            print("Le Bot à gagné")
            pointBot = pointBot + 1
            print(" ")
            print("Score :")
            print("Le Bot à :",pointBot)
            print(pseudoJou+" à :",pointJoueur)
            print(" ")

        elif choixJoueurGame == "ciseaux" and choixBotGame == "feuille" :
            print(" ")
            print("Le Joueur à gagné")
            pointJoueur = pointJoueur + 1
            print(" ")
            print("Score :")
            print("Le Bot à :",pointBot)
            print(pseudoJou+" à :",pointJoueur)
            print(" ")

        elif choixJoueurGame == "ciseaux" and choixBotGame == "pierre" : 
            print(" ")
            print("Le Bot à gagné")
            pointBot = pointBot + 1
            print(" ")
            print("Score :")
            print("Le Bot à :",pointBot)
            print(pseudoJou+" à :",pointJoueur)
            print(" ")

menu()






    



