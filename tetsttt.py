import random
from random import randint
pseudoJou = input("Choisi ton pseudo : ")
nombreDeManche = 1

def menu(): 
    print("Bienvenue dans le PFC, si tu veux jouer appuis sur 1 sinon appuie sur deux")
    choixMenu = input("Ton choix :")
    if choixMenu == "Jouer" :
        print("Jouer")
        game()
    else:
        print("Tampis")

def joueur():
    pseudoJoueur = pseudoJou
    choixJoueur = (input((pseudoJoueur +" Tu choisie quelle objets ")))
    pierre = 0
    ciseau = 0
    feuille = 0
    if choixJoueur == "pierre": 
        pierre = 1 
        if pierre == 1:
            print(pseudoJoueur +" à choisi Pierre")
    elif choixJoueur == "ciseaux" : 
        ciseau = 1 
        if ciseau ==1:
            print(pseudoJoueur +" à choisi ciseaux")
    elif choixJoueur == "feuille": 
        feuille = 1 
        if feuille ==1:
            print(pseudoJoueur +" à choisi feuille")
    elif choixJoueur != "pierre" or choixJoueur != "feuille" or choixJoueur != "ciseaux" :
        print("Erreur : Tu n'as pas choisi la bonne valeur")
        choixJoueur = input((pseudoJoueur +" Tu choisie quelle objets "))
    return choixJoueur
    

def option(nombreDeManche):
    nombreDeManche = input(("Tu veux jouer combien de manche ?"))
    return int(nombreDeManche)
    

def bot():
    tableau = ["pierre","feuille","ciseaux"]
    choixBot = tableau[randint(0,2)]
    pierre = 0
    ciseau = 0
    feuille = 0
   
    if choixBot == 0: 
        pierre = 1 
        if pierre == 1:
            print("BOT à choisi Pierre")
    if choixBot == 1 : 
        ciseau = 1 
        if ciseau ==1:
            print("BOT à choisi ciseau")
    if choixBot == 2: 
        feuille = 1 
        if feuille ==1:
            print("BOT à choisi feuille")
    return choixBot

def game(): 
 
    pointJoueur = 0 
    pointBot = 0   
    while nombreDeManche == 1 :
        choixJoueurGame = joueur()
        choixBotGame = bot()
        print("Le joueur à :",pointBot)
        print("Le joueur à :",pointJoueur)
        
        if pointJoueur or pointBot  == nombreDeManche :
            relancerUnePartie = False
        if pointJoueur or pointBot  == nombreDeManche :
            print("Tu veux rejouer ?")

        if choixJoueurGame == choixBotGame: 
            print("Egalité") 

        elif choixJoueurGame == "pierre" and choixBotGame == "feuille" : 
            print("Le Bot à gagné")
            pointBot = pointBot + 1
        elif choixJoueurGame == "pierre" and choixBotGame == "ciseaux" : 
            print("Le Joueur à gagné")
            pointJoueur = pointJoueur + 1
        
        elif choixJoueurGame == "feuille" and choixBotGame == "pierre" : 
            print("Le Joueur à gagné")
            pointJoueur = pointJoueur +1 
        elif choixJoueurGame == "feuille" and choixBotGame == "ciseaux" : 
            print("Le Bot à gagné")
            pointBot = pointBot +1 

        if choixJoueurGame == "ciseaux" and choixBotGame == "feuille" : 
            print("Le Joueur à gagné")
            pointJoueur = pointJoueur + 1
        if choixJoueurGame == "ciseaux" and choixBotGame == "pierre" : 
            print("Le Bot à gagné")
            pointBot = pointBot + 1

menu()






    


