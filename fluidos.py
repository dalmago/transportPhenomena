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

try:
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Button
    import numpy as np
except ImportError:
    print ("Verifique se você possui a biblioteca matplotlib e numpy instaladas.")
    print ("Caso contrário, instale-as com 'sudo apt-get install python-matplotlib python-numpy' (debian)")
    raise SystemExit

density1 = float(input("Densidade do fluido 1 [kg/m³]: "))
density2 = float(input("Densidade do fluido 2[kg/m³]: "))

x = np.arange(0,20,0.01)
y1 = x*density1*9.8
y2 = x*density2*9.8

class Type:
    def __init__(self):
        self.unityIndex = 0

    def change(self, event):
        if self.unityIndex == 0:
            self.unityIndex = 1
            self.pascal()
        else:
            self.unityIndex = 0
            self.atm()

    def pascal(self):
        ax1.cla()
        ax1.plot (x, y1*10**(-3), label='fluido 1', linewidth=2)
        ax1.plot (x, y2*10**(-3), label='fluido 2', linewidth=2)

        ax1.grid(True)
        ax1.legend()
        ax1.set_xlabel('Height [m]')
        ax1.set_ylabel('Pressure [kPa]')

    def atm(self):
        ax1.cla()
        ax1.plot (x, y1*9.87*10**(-6),\
                label='fluido 1', linewidth=2)
        ax1.plot (x, y2*9.87*10**(-6), \
                label='fluido 2', linewidth=2)

        ax1.grid(True)
        ax1.legend()
        ax1.set_xlabel('Height [m]')
        ax1.set_ylabel('Pressure [atm]')

fig = plt.figure()
ax1=fig.add_subplot(111)
plt.ion()

button = Button(ax1, 'click')
unity = Type()
button.on_clicked(unity.change)

plt.show()
