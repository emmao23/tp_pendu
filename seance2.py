#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:58:10 2020

@author: emmaortiz
"""

from Tkinter import *
import random as rd


def liste_mots(fichier):
    a = open('mots.txt','r')
    mots = a.readlines()
    nb_mots = len(mots)
    a.close()
    return (nb_mots)

def choix_mots(nb_mots):
   """
   cette fonction permet de choisir aléatoirement un mot dans le fichier texte
   """
   mot = rd.randint(0,nb_mots)
   a = open('mots.txt','r')
   for i in range(mot):
       a.readline()
   mot = a.readline()
   a.close()
   return mot.strip()


def affichage_mot(mot, lettres_t):
    """
    cette focntion permet d'afficher le mot à découvrir avec les _ _ _
    """    
    a=""
    for i, l in enumerate(mot):
        if i==0 or l in lettres_t:
            a+=l
        else:
            a+=" _ "
    print a

def gagne(mot_a_deviner, lettres_trouvees):
   """
   cette fonction permet de savoir si on a gagné le jeu
   """ 
   i=0
   for j in mot_a_deviner:
       if j in lettres_trouvees:
           i= i+1
   if i==len(mot_a_deviner):
       return True 
    

def affichage_lettre_f(lettres_f):
    """
    cette fonction permet de mettre de côté les lettres déjà essayées et de les laisser visible pour le joueur
   """
    F=""
    for i in lettres_f:
        F+=i
        F+=" "
    List.set("Lettres fausses : " +F)
    return F
    
def affichage_bonhomme():
    """
    cette fonction permet d'afficher le dessin du pendu après chaque lettre proposée
    """
    global nb_chance
    if nb_chance==6:
        item=Canevas.create_image(150, 150, image=image2)
    if nb_chance==5:
        item=Canevas.create_image(150, 150, image=image3)
    if nb_chance==4:
        item=Canevas.create_image(150, 150, image=image4)
    if nb_chance==3:
        item=Canevas.create_image(150, 150, image=image5)
    if nb_chance==2:
        item=Canevas.create_image(150,150, image=image6)
    if nb_chance==1:
        item=Canevas.create_image(150, 150, image=image7)
    if nb_chance==0:
        item=Canevas.create_image(150, 150, image=image8)
           
        
def verification ():
    """
    Cette fonction vérifie si la lettre proposée par l'utilisateur est dans le mot à trouver
    """
    global lettres_t, lettres_f, mot, nb_chance
    l=lettre.get()
    lettre.set('')
    if l in lettres_t or l in lettres_f:
        info.set("Vous avez déjà donné cette lettre")
    elif l in mot:
        lettres_t.append(l)
        affichage_mot(mot, lettres_t)
        info.set("Continuez, il manque encore des lettres")
    else:
        nb_chance= nb_chance - 1
        lettres_f.append(l)
        affichage_bonhomme()
        compt1.set("Nombre de coups restants : "+str(nb_chance))
        info.set("Dommage c'est raté")
        affichage_lettre_f(lettres_f)
        
def pendu():
    """
    cette fonction permet de jouer au pendu
    """
    global mot, lettres_t, lettres_f, nb_chance
    affichage_mot(mot, lettres_t)
    if nb_chance>0:
        verification()
        if gagne(mot, lettres_t)==True:
            info.set("Vous avez gagné !")
    if nb_chance==0 and gagne(mot, lettres_t)!=True:
        info.set("Vous avez perdu")

def rejouer ():
    """
     cette fonction permet de rejouer une partie si on le souhaite
     """
    global mot, lettres_t, lettres_f, nb_chance
    nb_mots=liste_mots('mots.txt')
    mot=choix_mots(nb_mots)
    lettres_t=mot[0]
    lettres_f=[]
    nb_chance=7
    pendu()
    return mot, lettres_t, lettres_f, nb_chance

nb_mots=liste_mots('mots.txt')
mot=choix_mots(nb_mots)
lettres_t=[mot[0]]
lettres_f=[]
nb_chance=7

Mafenetre=Tk()
Mafenetre.title('Jeu du pendu')



image1=PhotoImage(master=Mafenetre, file='bonhomme1.gif')
image2=PhotoImage(master=Mafenetre, file='bonhomme2.gif')
image3=PhotoImage(master=Mafenetre, file='bonhomme3.gif')
image4=PhotoImage(master=Mafenetre, file='bonhomme4.gif')
image5=PhotoImage(master=Mafenetre, file='bonhomme5.gif')
image6=PhotoImage(master=Mafenetre, file='bonhomme6.gif')
image7=PhotoImage(master=Mafenetre, file='bonhomme7.gif')
image8=PhotoImage(master=Mafenetre, file='bonhomme8.gif')

largeur=300
hauteur=300
Canevas=Canvas(Mafenetre, height=hauteur, width=largeur, bg='white')
item=Canevas.create_image(150, 150, image=image1)

lettre=StringVar()
bouton_entry=Entry(Mafenetre, textvariable=lettre)

#création du bouton "Proposer" pour proposer une lettre 
bouton_proposer=Button(Mafenetre, text='Proposer', command= pendu)

#création du boutton "Rejouer" pour pouvoir rejouer
bouton_rejouer=Button(Mafenetre, text='Rejouer', command=rejouer)

#création du bouton "Quitter" pour quitter le jeu 
bouton_quitter=Button(Mafenetre, text='Quitter', command=Mafenetre.destroy)

#creation d'un label pour afficher le mot à trouver avec les _ _ _ 
a=StringVar()
a.set("Mot à trouver : " +affichage_mot(mot, lettres_t))
label_mot_rech=Label(Mafenetre, textvariable=a, fg='black', bg='white')

#creation d'un label pour afficher la liste des lettres poroposées qui sont fausses 
List=StringVar()
label_lettres_f=Label(Mafenetre, textvariable=List, fg='black', bg='white')

#creation d'un label pour afficher le nombre de coups restants
compt1=StringVar()
compt1.set("Nombre de coups restants : " + str(nb_chance))
label_coups=Label(Mafenetre, textvariable=compt1, fg='black', bg='white')

#creation d'un label qui affiche des commentaires comme Bravo ! ou Dommage !
info=StringVar()
console=Label(Mafenetre, textvariable=info, fg='black', bg='white')

label_coups.grid(row=1, sticky=NE)
label_mot_rech.grid(row=2)
bouton_entry.grid(row=3)
bouton_proposer.grid(row=4)
bouton_rejouer.grid(row=5)
bouton_quitter.grid(row=6)
label_lettres_f.grid(row=7)
Canevas.grid(row=1, column=2, rowspan=6)
console.grid(row=7, column=2)


Mafenetre.mainloop()