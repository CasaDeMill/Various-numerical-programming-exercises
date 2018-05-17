# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 22:21:46 2016

@author: artin
"""
from scipy import *
from pylab import *
import sys


class Animal:
    def __init__(self, sex, name, color):
        self.sex=sex
        self.name=name
        self.color=color
    
Pupper = Animal("Male", "DOGGO", "White")


