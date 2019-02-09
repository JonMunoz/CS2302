#Jon Munoz
#CS2302 Data Structures
#Lab 1
#Instructor:Olac Fuentes
#TA:Anindita Nath
#Last Modified 2/8/19

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
fig, ax2 = plt.subplots()#second plane for second shape
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')

#method to draw shape number 2
#counter controls my number of recursive calls, xcent is the center point of my circles
#scale controls the rate at which the circles shrink
def draw_shape1(counter, xcent, scale):
    if counter == 0:#base case for when counter hits 0
        print()
    else:
        draw_circles(ax, 1, [xcent, 0], xcent, .9)#draws the circle for each call to the method(including recursive calls)
        draw_shape1(counter-1, (xcent*scale), scale)#recursively calls the method while shrinking the circle in each call

#method call for shape1
draw_shape1(10, 100, .6)

#method to draw shape number 4
#levelRec controls my number of recursive calls, x and y is the center point of my circles
#scale controls the rate at which the circles shrink
def draw_shape2(levelRec, x,y, rad):
    if levelRec == 0:#base case for when levelRec hits 0
        print()
    else:
        draw_circles(ax2, 1, [x,y], rad, .9)#draws the circle
        draw_shape2(levelRec - 1, x, y, rad*(1/3)) #middle circle recursive call
        draw_shape2(levelRec - 1, x, y-((2/3)*rad), rad*(1/3)) #bottom cricle recursive call
        draw_shape2(levelRec - 1, x, y+((2/3)*rad), rad*(1/3)) #top circle recursive call
        draw_shape2(levelRec - 1, x-((2/3)*rad), y, rad*(1/3)) #left circle recursive call
        draw_shape2(levelRec - 1, x+((2/3)*rad), y, rad*(1/3)) #right circle recursive call

#method call for shape2
draw_shape2(4, 500,500, 500)