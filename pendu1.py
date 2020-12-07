#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:07:21 2020

@author: emmaortiz
"""

from seance1 import liste_mots
nb_mots = liste_mots("mots.txt")

from seance1 import choix_mots
mot_a_deviner=choix_mots(nb_mots)

from seance1 import pendu
pendu()
