#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:41:05 2019

@author: mtslazarin
"""

#%% Importando bibliotecas
import pytta
 
#%% Gerando sweep
sweep = pytta.generate.sweep()

#%% Tocando sweep
sweep.play()

#%% Time plot
sweep.plot_time()

#%% Frequency plot
sweep.plot_freq()