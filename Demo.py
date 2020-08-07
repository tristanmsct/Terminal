#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:52:53 2020.

@author: tristan
"""

# Packages
from terminal import InputManager as term

# %%

# Chacune des fonctions de lecture s'utilise de la même manière, avec un prompt et des conditions.

int_res = term.read_numeric('Entrez un chiffre en 1 et 10 :\n', bool_int=True,
                            num_borne_inf=1, num_borne_sup=10, bool_bi_incluse=True, bool_bs_incluse=True)

print(int_res)

# %%

# Saisie libre
term.read_line('Quel est votre nom ?\n', bool_case=False, set_char=None)

# Saisie sous contrainte
term.read_line('Quel est votre fruit préféré ?\n', bool_case=False, set_char=['Pomme', 'Poire'])

# %%

# Lit oui ou non dans ['y', 'n', 'o', 'yes', 'no', 'oui', 'non']
term.read_yes_no('Continuer ? [y/n]\n')

# Lit oui ou non et retourne un booléen dans ['y', 'n', 'o', 'yes', 'no', 'oui', 'non',
#                                             'T', 'F', 'V', 'False', 'True', 'Vrai', 'Faux']
term.read_true_false('Continuer ? [y/n]\n')

