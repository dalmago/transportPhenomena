#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#"THE BEER-WARE LICENSE" (Revision 42):
#
#<matheusdalmago10@hotmail.com> wrote this file. As long as you retain this
#notice you can do whatever you want with this stuff. If we meet some day,
#and you think this stuff is worth it, you can buy me a beer in return.
#
#Created: 2014-05-13
#       by: Matheus Dal Mago
#
# Read the density of two fluids and plot the graph height X pressure

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,40,0.01)

density1 = int(input("Densidade do primeiro fluido [kg/m³]: "))
density2 = int(input("Densidade do segundo fluido [kg/m³]: "))

plt.grid(True)
plt.xlabel('Height [m]')
plt.ylabel('Pressure [Pa]')

plt.plot (x, x*density1*9.8, label='fluido 1', linewidth=2)
plt.plot (x, x*density2*9.8, label='fluido 2', linewidth=2)

plt.legend()
plt.show()
