#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Program 2 for the Git/Github class exercise.
'''

import math

def val_absoluto(a):
    '''Este programa retorna el valor absoluto de a'''
    return abs(a)

def div_entero(a,b):
    '''Este programa retorna el valor entero de la division entre a y b'''
    if b!=0:
    	c=int(a/b)
    else:
    	c='b=0 no se puede dividir'
    return c

def div_resto(a,b):
	pass

def cubo(a):
    '''Este programa calcula el cubo de la variable a'''
    return a*a*a

def log10(a):
    '''Este programa devuelve el log en base 10 de a'''
    return math.log10(a)
