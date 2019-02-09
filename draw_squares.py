#Jon Munoz
#CS2302 Data Structures
#Lab 1
#Instructor:Olac Fuentes
#TA:Anindita Nath
#Last Modified 2/8/19

import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q,w)

plt.close("all") 
orig_size = 800
fig, ax = plt.subplots()
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')


#method for square shape
#levelRec controls the level of recursion, x and y control the midpoint of each square 
#halfW is the distance between the midpoint and a side of the square
def draw_shape(levelRec, x, y, halfW):
    if levelRec == 0:#base case for when levelRec hits 0
        print()
    else:
        # p = ........ sets the points for the square
        p = np.array([[x-halfW,y-halfW],[x-halfW,y+halfW],[x+halfW,y+halfW],[x+halfW,y-halfW],[x-halfW,y-halfW]])
        draw_squares(ax, 1, p,.5)#draw out the square with the oints from p
        draw_shape(levelRec - 1, x-halfW, y-halfW, halfW/2)#bottom left square recursive call, while decreasing halfW by 2 to make square smaller
        draw_shape(levelRec - 1, x-halfW, y+halfW, halfW/2)#top left square recursive call, while decreasing halfW by 2 to make square smaller
        draw_shape(levelRec - 1, x+halfW, y+halfW, halfW/2)#top right square recursive call, while decreasing halfW by 2 to make square smaller
        draw_shape(levelRec - 1, x+halfW, y-halfW, halfW/2)#bpttom right square recursive call, while decreasing halfW by 2 to make square smaller
        
#method call 
draw_shape(4, 100, 100, 50)
    