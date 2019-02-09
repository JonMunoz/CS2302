#Jon Munoz
#CS2302 Data Structures
#Lab 1
#Instructor:Olac Fuentes
#TA:Anindita Nath
#Last Modified 2/8/19

import numpy as np
import matplotlib.pyplot as plt

def draw_triangle(ax,n,p,w):
    if n>0:
        i1 = [1,0,1]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_triangle(ax,n-1,q,w)

plt.close("all") 
orig_size = 1000
fig, ax = plt.subplots()
ax.set_aspect(.5)#set aspect ratio to .5 to make the figure not seem so small
ax.axis('off')
plt.show()
fig.savefig('tree.png')

#my method that draws the tree where each leaf gets smaller
#counter controls my levels of recursion, x and y are my coordinates, height I use to control the height of my tree
#and rad is the "radius" of my triangles, since my original point is the middle bottom of my triangle I use rad to control the 
#distance that my bottom two x points are from the center 
def draw_tree(counter, x, y, height, rad): 
    if counter == 0:#base case for when my counter reaches 0
        print()
    else:
        p = np.array([[x-rad,y],[x, y+height],[x+rad,y]])#this line sets the points for my triangle
        draw_triangle(ax, 1, p,.9)#this line draws the triangle
        draw_tree(counter - 1, x-rad, y-height, height, rad/2)#recursive call that sets the next triangle to the bottom left and makes it smaller
        draw_tree(counter - 1, x+rad, y-height, height, rad/2)#recursive call that sets the next triangle to the bottom right and makes it smaller
    
draw_tree(7, 10, 10, 10, 10)#method call

