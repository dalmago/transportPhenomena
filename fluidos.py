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
#Created: 2014-05-13                                                           
#       by: Matheus Dal Mago                                                   
#                                                                              
# Read the density of two fluids and plot the graph height x pressure          
                                                                               
import matplotlib.pyplot as plt                                                
import numpy as np                                                             
                                                                               
x = np.arange(0,20,0.01)                                                       
densidade = int(input("digite "))                                              
                                                                               
plt.grid(True)                                                                                          
                                                                                  
plt.plot(x, x*densidade*9.8, label="primeiro")                                    
                                                                               
plt.show() 