import random

choixJoueurTest = input()
choixBotTest = random.randint(1, 3)
nombreDeMancheTest = input()

def joueur (choixJoueur):
    choixJoueur = choixJoueurTest
    print("Tu choisie quelle objets ?")
    pierre = 0
    ciseau = 0
    feuille = 0
    if choixJoueurTest == 1: 
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
    

def option(nombreDeManche):
    print("Combien de manche souhaite tu jouer ?")
    nombreDeManche = nombreDeMancheTest
    

def bot (choixBot):
    choixBot = choixBotTest
    pierre = 0
    ciseau = 0
    feuille = 0
    if choixBot == 1: 
        pierre = 1 
        if pierre ==1:
            print("BOT à choisi Pierre")
    if choixBot == 2 : 
        ciseau = 1 
        if ciseau ==1:
            print("BOT à choisi ciseau")
    if choixBot == 3: 
        feuille = 1 
        if feuille ==1:
            print("BOT à choisi feuille")

def game (choixJoueur,ChoixBot): 
    choixJoueur = choixJoueurTest
    choixBot = choixBotTest
    pointJoueur= 0 
    pointBot = 0
    relancerUnePartie = True
    nombreDeManche = 0
    option(nombreDeMancheTest)
    while pointJoueur < nombreDeManche and pointBot < nombreDeManche and relancerUnePartie == True:
        joueur(choixJoueurTest)
        bot(choixBotTest)
        print("hello ")
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

game(choixJoueur,choixBotTest)






    



