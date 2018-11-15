#weierstrass
import sys
import matplotlib.pyplot as plt
import math
import cmath

import numpy as np
import matplotlib as mpl
mpl.style.use('dark_background')
#mpl.style.use('seaborn')
import matplotlib.animation as animation
import os
import matplotlib.cm as cm
import random

#parameters start
a = 2.2
b = .2
N = 50 #? ? idk
#bound = dx
dx = 1000
yrefmin = -1.5
yrefmax = 1.5
#steps = 20000 #resolution
bound =dx*(1/2-.3)#+- x bounds
offset = .9
#steps = int(bound*2/30*dx)
dxScalar = .999
#dxScalar = .9
steps = 3000
movie_name = "weistrauss"
x0 = 4
#parameters end



pi = math.pi
w = [0]*steps
i = np.arange(steps)
n = np.arange(N+1)
an = (a**n)[np.newaxis]
bn = (b**n)[np.newaxis]

#w = np.array([0]*steps)
i = np.arange(steps)
#graph = plt.step(i,w)[0]
#plt = step
#a = 2.2
#b = .6
#N = 50
#steps = 2k
#dx = 1k
#view x0 +-1

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
graph = ax.plot(i,w)[0]
wprev = (np.array([0]*steps)[np.newaxis]).T
#print("wprev:"+str(wprev.shape))

ymin = yrefmin
ymax = yrefmax
fig.suptitle("Weierstrass function")



Writer = animation.writers['ffmpeg']
writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)

plt.ion()

movie_dir = 'animations' #please only be 1 level, or separated by /, thanks.
for directory in movie_dir.split('/'):
    try:
        os.chdir(directory)
    except:
        os.mkdir(directory)
        os.chdir(directory)

files = os.listdir()
movie_exists = True
animation_number = 1
movie_name_custom = movie_name

color_theta = 0
T_theta = wprev.shape[0]
dtheta = (2*pi)/T_theta

while(movie_exists): 
    movie_exists = any(movie_name_custom in s for s in files)
    if(movie_exists):
        movie_name_custom = movie_name + str(animation_number)
        animation_number = animation_number + 1

with writer.saving(fig, movie_name_custom + ".mp4", 100):
    while(dx>900):
        


        x = ((x0 - dx) + (2*dx)*i/steps)[np.newaxis]
        theta = (pi*an*(x.T))
        cos = np.cos(theta)
        w = np.dot(cos,bn.T)
        #idx = np.random.permutation((w.shape[0]))
        #colors = random.shuffle(cmap)
        #print(colors)
        #w = ((w+wprev)/2)
        #wprev = np.copy(w)

        #graph.set_xdata(x.T)
        #graph.set_ydata(w)
        plt.cla()
        num = abs(((cmath.phase(cmath.exp(-2j*pi*13/50)))/(pi)))+.01
        print(num)
        num = int(num*16777200*.98)
        color = ('#' + '%06x' % num)
        #color_theta = color_theta + 1
        ax.plot(x.T,w,color=color, alpha=0.5)
        ax.set_title("a = " + str(a) + ", b = "+ str(b)+ ", resolution/startingwidth = 2000/1000")# + str(cnt))
        ax.set_ylabel('w(x)')
        ax.set_xlabel('x, dx = ' + str(dx))

        #plt.ylim(-3,3)
        #ymin = ymin - min(w)[0]*(yrefmin-ymin)
        #ymax = ymax - max(w)[0]*(yrefmax-ymax)

        #ymin = ymin + (1-dxScalar)*(yrefmin-ymin*min(w)[0])
        #ymax = ymax + (1-dxScalar)*(yrefmax-ymax*max(w)[0])

        ax.set_ylim(ymin,ymax)

        #plt.xlim((x0 - dx),(x0 + dx))
        #plt.xlim((x0 - bound),(x0 + bound))
        
        ax.set_xlim((x0 - bound*offset),(x0 + bound*offset))

        #fig.canvas.draw()
        writer.grab_frame()
        plt.pause(0.00001) #uncomment to watch the plot live

        dx = dx*dxScalar
        bound =dx*(1/2-.3)#+- x bounds


