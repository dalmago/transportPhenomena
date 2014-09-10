#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#"THE BEER-WARE LICENSE" (Revision 42):
#
#<matheusdalmago10@hotmail.com> wrote this file. As long as you retain this
#notice you can do whatever you want with this stuff. If we meet some day,
#and you think this stuff is worth it, you can buy me a beer in return.
#
#Created: 1014-05-13
#       by: Matheus Dal Mago
#

try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print ("Verifique se você possui as bibliotecas matplotlib e numpy instaladas.")
    raise SystemExit

"""
    Temperatuda das superfícies
"""
tempS = 500

"""
    Temperatura da corrente de ar
"""
tempInf = 300

"""
    Coeficiente de conveccao
"""
h = 10

"""
    Lado malha
"""
xy = 0.25

"""
    Das equacoes 4.29 e 4.42:
"""
A = np.matrix([
    [-4, 1, 1, 0, 0, 0, 0, 0],
    [2, -4, 0, 1, 0, 0, 0, 0],
    [1, 0, -4, 1, 1, 0, 0, 0],
    [0, 1, 2, -4, 0, 1, 0, 0],
    [0, 0, 1, 0, -4, 1, 1, 0],
    [0, 0, 0, 1, 2, -4, 0, 1],
    [0, 0, 0, 0, 2, 0, -9, 1],
    [0, 0, 0, 0, 0, 2, 2, -9]])

C = -np.matrix([
    [2*tempS],
    [tempS],
    [tempS],
    [0],
    [tempS],
    [0],
    [tempS + 2*(h*xy)*tempInf],
    [2*(h*xy)*tempInf]])

"""
    Resolvendo por inversao de matrizes
"""
T = np.linalg.inv(A)*C

print ("Temperatura nos pontos 1 a 8:")
print (T)
T = T.A1

"""
    Taxa de transferencia de calor
"""
taxa = 2*h*(((xy/2)*(tempS-tempInf))+ xy*(T[6]-tempInf)+((xy/2)*(T[7]-tempInf)))

print ("Taxa de transferencia de calor:")
print (taxa)

"""
    Normalizando vetor de temperaturas (para plotagem) e plotando
"""
T = (T/500) 

tempFinal = np.matrix([
            [1, 1, 1, 1, 1],
            [1, T[0], T[1], T[0], 1],
            [1, T[2], T[3], T[2], 1],
            [1, T[4], T[5], T[4], 1],
            [1, T[6], T[7], T[6], 1]])

plt.imshow(tempFinal, interpolation='gaussian')
plt.show()
