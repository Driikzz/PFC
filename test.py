import random

choixJoueur = input()
choixBot = random(1,3)
def joueur (choixJoueur):
    choixJoueur = input()
    pierre = 0
    ciseau = 0
    feuille = 0
    if choixJoueur == 1: 
        pierre = 1 
        if pierre ==1:
            print("Joueur à choisi Pierre")
    elif choixJoueur == 2 : 
        ciseau = 1 
        if ciseau ==1:
            print("Joueur à choisi ciseau")
    elif choixJoueur == 3: 
        feuille = 1 
        if feuille ==1:
            print("Joueur à choisi feuille")
    return(choixJoueur)

def option(nombreDeManche):
    print("Combien de manche souhaite tu jouer ?")
    nombreDeManche = input()

def bot (choixBot):
    choixBot = random(1,3)
    pierre = 0
    ciseau = 0
    feuille = 0
    if choixBot == 1: 
        pierre = 1 
        if pierre ==1:
            print("BOT à choisi Pierre")
    elif choixBot == 2 : 
        ciseau = 1 
        if ciseau ==1:
            print("BOT à choisi ciseau")
    elif choixBot == 3: 
        feuille = 1 
        if feuille ==1:
            print("BOT à choisi feuille")
    return choixBot

def game (choixJoueur,ChoixBot): 
    choixJoueur = joueur(input())
    choixBot = bot(random(1,3))
    pointJoueur= 0 
    pointBot = 0
    relancerUnePartie = True
    nombreDeManche = 0
    option()
    while pointJoueur < nombreDeManche & pointBot < nombreDeManche & relancerUnePartie == True:
        bot()
        joueur()

        if pointJoueur | pointBot  == nombreDeManche :
            relancerUnePartie = False
        if pointJoueur | pointBot  == nombreDeManche :
            print("Tu veux rejouer ?")

        if choixJoueur == choixBot: 
            print("Egalité") 

        if choixJoueur == 1 & choixBot == 2 : 
            print("Le Bot à gagné")
            pointBot + 1
        if choixJoueur == 1 & choixBot == 3 : 
            print("Le Joueur à gagné")
            pointJoueur + 1
        
        if choixJoueur == 2 & choixBot == 1 : 
            print("Le Joueur à gagné")
            pointJoueur + 1
        if choixJoueur == 2 & choixBot == 3 : 
            print("Le Bot à gagné")
            pointBot + 1

        if choixJoueur == 3 & choixBot == 2 : 
            print("Le Joueur à gagné")
            pointJoueur + 1
        if choixJoueur == 3 & choixBot == 1 : 
            print("Le Bot à gagné")
            pointBot + 1




    



