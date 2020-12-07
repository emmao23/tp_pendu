#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:07:21 2020

@author: emmaortiz
"""

"""
Header:
    Objectif: Réalisation d'un jeu du pendu
    Date: 30/11/2020
    Par: Emma Ortiz (Groupe C)
"""

import random as rd

def liste_mots(fichier):
    a = open('mots.txt','r')
    mots = a.readlines()
    nb_mots = len(mots)
    a.close()
    return (nb_mots)

def choix_mots(nb_mots):
    mot = rd.randint(0,nb_mots)
    a = open('mots.txt','r')
    for i in range(mot):
        a.readline()
    mot = a.readline()
    a.close()
    return mot.strip()


def affichage_mot(mot, lettres_trouvees):
    for i, l in enumerate(mot):
        if i==0 or l in lettres_trouvees:
            print(l)
        else:
            print(" _ ")

def appel_lettre():
    lettre=raw_input("Donnez une lettre")
    return lettre
    
def gagne(mot_a_deviner, lettres_trouvees):
    i=0
    for j in mot_a_deviner:
        if j in lettres_trouvees:
            i= i+1
    if i==len(mot_a_deviner):
        return True 
    
def pendu():
    i=8
    nb_mots=liste_mots("mots.txt")
    mot_a_deviner=choix_mots(nb_mots)
    lettres_trouvees=[mot_a_deviner[0]]
    lettres_fausses=[]
    affichage_mot(mot_a_deviner, lettres_trouvees)
    while i>0:
        lettre=appel_lettre()
        if lettre in lettres_trouvees or lettre in lettres_fausses:
            print ("Vous avez déjà donné cette lettre")
        if lettre in mot_a_deviner:
            lettres_trouvees.append(lettre)
            affichage_mot(mot_a_deviner, lettres_trouvees)
            print("Bravo, cette lettre est dans le mot et il vous reste", i,"chances")
        else:
            i=i-1
            lettres_fausses.append(lettre)
            print("Dommage, cette lettre n'est pas dans le mot et il vous reste",i,"chances")
        if gagne(mot_a_deviner, lettres_trouvees)==True:
            print("Vous avez gagné")
            score=i
            i=0
        else: 
            print("Essayez encore")
    if i==0 and gagne(mot_a_deviner, lettres_trouvees)!=True:
        print("Vous avez perdu")
    if i==0:
        rejouer=input("Tapez 1 pour rejouer, 2 sinon")
        if rejouer==1:
            return score, pendu()
        else:
            print ("Votre score est de", score)
            return score
        
def meilleur_score(best):
    score=pendu()
    if score > best:
        best=score
        print("Vous avez le meilleur score")
        
        
        
    
    

