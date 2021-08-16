#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:31:06 2021

@author: dr.guillermo
"""

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
x=np.linspace(-np.pi,np.pi,11)
y=np.linspace(-np.pi,np.pi,11)

#malla
xmesh,ymesh = np.meshgrid(x,y)

def f(x,y,t):
    return np.sin(y+t)*np.cos(x)
    
#zmesh=f(xmesh,ymesh,t)
# fig vacia
fig= plt.figure()
#tomamos los ejes
ax= fig.gca(projection='3d')

#actualizar la fig
#con el iterador
def actualizar(i):
    ax.clear() # borrar ejex
    zmesh=f(xmesh,ymesh,t[i])
    ax.plot_surface(xmesh,ymesh, zmesh) #va punto por punto
    plt.title(str(t[i]))
    #plt.xlim(min(x),max(x))
    #plt.ylim(min(y),max(y))
    #plt.zlim(-1.5,1.5)
    
#animacion
ani=animation.FuncAnimation(fig, 
                            actualizar,
                            range(len(t)),
                            interval=10,
                            repeat=True)
plt.show()
