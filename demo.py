#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:52:53 2020.

@author: Tristan Muscat
"""

# Packages
from terminal import InputManager as im

# %% Read line function

# Open question
str_name = im.read_line('What is your name ?\n')
print(f'Hello, {str_name}.')

# Closed question
str_fruit = im.read_line('Do you prefere apples or pears ?\n', bl_case=False, lst_values=['Apples', 'Pears'])
print(f'I too like {str_fruit.lower()} :).')

# %% Yes or No questions

# By default recognize (yes, y, oui and o) as yes, and (no, n and non) as no.
im.read_yes_no('Proceed ? [y/n]\n')

# This can be changed
im.read_yes_no('Continuar ? [Si/No]\n', lst_pos_vals=['Si', 's'], lst_neg_vals=['No', 'n'])

# %% Read numeric

# Basic numeric read
int_res = im.read_numeric('Choose a numer :\n')
print(f'You chose {int_res}.')

# This function can be tweaked with some parameters :

int_res = im.read_numeric('Choose a number between 1 and 10 :\n', bl_int=True,
                          num_lb=1, num_ub=10, bl_inc_lb=True, bl_inc_ub=True)
print(f'You chose {int_res}.')

# %% Force read

# In order not to crash on a bad input, you can use the force_read function
int_res = im.force_read(im.read_numeric, 'Choose a number between 1 and 10 :\n', bl_int=True,
                        num_lb=1, num_ub=10, bl_inc_lb=True, bl_inc_ub=True)
print(f'You chose {int_res}.')
