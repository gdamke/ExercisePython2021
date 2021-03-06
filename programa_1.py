#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Program 1 for the Git/Github class exercise.
'''

import math

def suma(a,b):
    '''Este programa retorna el valor de la suma de a y b '''
    return a+b

def resta(a,b):
    '''Este programa retorna el valor de la resta de a y b'''
    return a-b 

def multiplicacion(a,b):
    '''Este programa retorna el valor de la multiplicación de a y b'''
    return a*b

def division(a,b):
   '''Este programa retorna el valor de la division de a y b'''
   if b!=0:
   	c=a/b
   else:
   	c='b=0 no se puede dividir'
   return c
   
def exponencial(a):
    '''Este programa retorna el valor de e elevado a la a potencia'''
    return math.exp(a)

def rama_raiz_cuadrada(a):
    ''''Este programa retorna la raiz cuadrada  de a'''
    return math.sqrt(a)

def cuadrado(a):
    '''Este programa retorna el valor del cuadrado de a'''
    return a*a
 
def lognatural(a):
    '''Este programa retorna el valor del logaritmo de a'''
    return math.log(a)   
