# DEBUT

# On admet la fontion random 
# On admet la la fonction Input 


# 
# Définir la fonction Joueur avec comme paramètre choixJoueur:
#    On assigne à la variable choixJoueur le retour de l'execution de Input du joueur
#    Initialise la variable pierre à 0
#    Initialise la variable ciseau à 0 
#    Initialise la variable feuille à 0 
#    Si choixJoueur est égale à 1 :
#       Alors assigne 1 à la variable pierre
#       Si pierre == 1: 
#           afficher choix du joueur est pierre
#    Sinon si choixJoueur est égale à 2 :
#       Alors Assigne 1 à la variable feuille
#       Si feuille == 1: 
#           afficher choix du joueur est feuille 
#    Sinon si choixJoueur est égale à 3 :
#       Alors Assigne 1 à la variable ciseau 
#       Si ciseau == 1: 
#           afficher choix du joueur est ciseau
#    retourner choixJoueur
#   
# Definir la fonction bot avec comme paramètre choixBot:
#   On assigne à la variable choixBot le retour de l'execution de la fonction random avec comme paramètre 0,3
#   Initialise la variable pierre à 0
#   Initialise la variable ciseau à 0 
#   Initialise la variable feuille à 0 
#   Si choixBot est égale à 1 alors :
#       Alors assigne 1 à la variable pierre 
#       Si pierre == 1: 
#           afficher choix du bot est pierre
#   Sinon si choixBot est égale à 2 :
#       Alors Assigne 1 à la variable feuille
#       Si pierre == 1: 
#           afficher choix du bot est feuille
#   Sinon si choixBot est égale à 3 :
#       Alors Assigne 1 à la variable ciseau
#       Si ciseau == 1: 
#           afficher choix du bot est ciseau
#   retourner choixBot

#Définir la fonction option avec comme paramètre nombreDeManche, relancerUnePartie:
#   dd




#Définir la fonction game avec comme paramètre (choixBot,ChoixJoueur):
#   On assigne à choixBot le retour de l'execution de Bot
#   On assigne à choixJoueur le retour de l'execution de Joueur
#   On initialise la variable pointJoueur à 0
#   On initialise la variable pointBot à 0
#   Tant que pointJoueur est plus petit que 3 et pointBot est plus petit que 3  :
#       Alors
#       On appelle et execute la fonction bot
#       On appelle et execute la fonction Joueur 
#       Si choixJoueur et choixBot sont égaux alors : 
#           On affiche "Egalité"
#
#       Si choixJoueur est égale à 1 et choixBot est égale à 2 : 
#           On affiche "Le bot à Gagné"
#           Ajoute 1 à la variable pointBot 
#       Si choixJoueur est égale à 1 et choixBot est égale à 3 :
#           On affiche Le joueur à gagné
#           Ajoute 1 à la variable pointJoueur 
#   
#       Si choixJoueur est égale à 2 et choixBot est égale à 1 :
#           On affiche Le joueur à gagné
#           Ajoute 1 à la variable pointJoueur 
#       Si choixJoueur est égale à 2 et choixBot est égale à 3 :
#           On affiche "Le bot à Gagné"
#           Ajoute 1 à la variable pointBot 

#       Si choixJoueur est égale à 3 et choixBot est égale à 2 :
#           On affiche Le joueur à gagné
#           Ajoute 1 à la variable pointJoueur 
#       Si choixJoueur est égale à 3 et choixBot est égale à 1 :
#           On affiche "Le bot à Gagné"
#           Ajoute 1 à la variable pointBot 

# FIN



