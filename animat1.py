#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:05:09 2021

@author: dr.guillermo
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation

# %matplolib auto  modo ventana
#            inline  modo iterativo 
x=np.linspace(0,4,101)

y=x**2

# fig vacia
fig= plt.figure()
#tomamos los ejes
ax= fig.gca()

#actualizar la fig
#con el iterador
def actualizar(i):
    ax.clear() # borrar ejex
    ax.plot(x[:i],y[:i]) #va punto por punto
    plt.title(str(x[i]))
    plt.xlim(min(x),max(x))
    plt.ylim(min(y),max(y))
    
#animacion
ani=animation.FuncAnimation(fig, 
                            actualizar,
                            range(len(x)),
                            interval=10,
                            repeat=False)
plt.show()