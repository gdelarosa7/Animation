#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:20:22 2021

@author: dr.guillermo
"""

#

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation

# %matplolib auto  modo ventana
#            inline  modo iterativo 
t=np.linspace(0,10,51)
x=np.linspace(-np.pi,np.pi,101)

def f(x,t):
    return np.sin(x+t)
    

# fig vacia
fig= plt.figure()
#tomamos los ejes
ax= fig.gca()

#actualizar la fig
#con el iterador
def actualizar(i):
    ax.clear() # borrar ejex
    ax.plot(x,f(x,t[i])) #va punto por punto
    plt.title(str(t[i]))
    plt.xlim(min(x),max(x))
    plt.ylim(-1.5,1.5)
    
#animacion
ani=animation.FuncAnimation(fig, 
                            actualizar,
                            range(len(t)),
                            interval=10,
                            repeat=False)
plt.show()