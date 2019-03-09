#Jon Munoz
#CS2302 Data Structures
#Lab 3
#Instructor:Olac Fuentes
#TA:Anindita Nath
#Last Modified 3/8/19


import numpy as np
import matplotlib.pyplot as plt


class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def inOrder(T):
    if T == None:
        return
    else:
        inOrder(T.left)
        print(T.item,end = ' ')
        inOrder(T.right)
        
def smallest(T):
    if T is None:
        return None
    t = T
    while t.left is not None:
        t = t.left
    return t
    
def smallestR(T):
    if T.left is None:
        return T
    return smallest(T.left)

def largestR(T): #can do something like t = T and use t in the rest
    if T.right is None:
        return T
    return largestR(T.right)

def find(T, key):
    if T is None or T.item == key:
        return T
    if T.item < key:
        find(T.right, key)
    return find(T.left,key)

#method counts the total number of nodes in given tree
def numNodes(T):
    if T == None:#if T is none then you want to return 0 since there are no nodes at this point 
        return 0
    else:
        count = 1
        if T.right != None:#if T.right is not None then you want to continue down that tree and continually add 1 until T is None
           count += numNodes(T.right)
        if T.left != None:#if T.left is not None then you want to continue down that tree and continually add 1 until T is None
           count += numNodes(T.left)
        return count#return count (the total number of nodes)

#gets the height of given tree
def getHeight(T):
    if T == None:#if T is none then then you want to return 0 since there is no more depth at this point
        return 0
    else:
        lHeight = getHeight(T.left)#lHeight gets the height of the left
        rHeight = getHeight(T.right)#rHeight gets the height of the right
        if lHeight > rHeight:#compare lHeight with rHeight and if lHeight is greater then you want to return lHeight plus 1 since lHeight went down further than rHeight
            return lHeight + 1
        else:
            return rHeight + 1#else rHeight was bigger so you return that
        
#Search method but done iteritively
def findIterative(T, key):
    while T.item != key:#as long as the item at the current node is not the key then you keep traversing
        if key < T.item:#if the key is less than the current item then you want to traverse the left subtree
            T = T.left
        elif key > T.item:#if the key is less than the current item then you want to traverse the right subtree
            T = T.right
    return T

#method creates a sorted list from a binary tree
def TtoL(T):
    if T == None:
        return []#return an empty list if T is equal to none since there is nothing in the node
    elif T != None:
        rootList = [T.item]#rootList is the list comprised of the root of the tree(or node)
        smallList = TtoL(T.left)#recursively calls the method with the left subtree and stores what it returns into smallList
        largeList = TtoL(T.right)#recursively calls the method with the right subtree and stores what it returns into largeList
    return smallList + rootList + largeList#return the concatenation of rootList, smallList, and moreList
        
    
#method creates a binary tree out of a sorted list
def LtoT(L):
    if(len(L)==0):
        return None
    elif len(L) > 0:#since the lenght must be greater than 0 to have contents this is the constraint
        mid =len(L)//2#mid is assigned to the length of the list divided by 2
        T = BST(L[mid])#puts the middle element of the list into the node of the tree
        T.left = LtoT(L[:mid])#recursively calls the LtoT method with the second half of the list 
        T.right = LtoT(L[mid + 1:])#recursively calls the LtoT method with the first half of the list
        return T

#This method prints all the items at a given depth
def printAtDepth(T, d):
    if T == None:#base case for when T is None
        return 
    if d == 0:#if d is 0 then you are at your desired depth and proceed to print the elements
        print(T.item, end = ' ')#prints the items on the given depth
    else:
        printAtDepth(T.right, d - 1)#traverses down the right tree to the given depth
        printAtDepth(T.left, d - 1)#traverses down the right tree to the given depth
        
#this method uses printAtDepth to print each depths items
def printAtDepth2(T, n):
    if T == None:
        return 
    if n != -1:#-1 since the depth can be 0
        for i in range(n):
            print()#this print statement seperates each of the below print statement
            print('Keys at depth',i,':', end = ' ')
            printAtDepth(T, i)#recursive call to the printAtDepth method 
        
    
#lines 131 - 144 are required to draw the tree shape
def draw_triangle(ax,n,p,w):
    if n>0:
        i1 = [1,0]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_triangle(ax,n-1,q,w)

plt.close("all") 
orig_size = 1000
fig, ax = plt.subplots()
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('tree.png')


#this method draws the BST
def draw_tree(T, x, y, height, deltaX):
    if T is not None:#continue with the below lines while T is not None since you dont want to make unnessecary lines
        plt.text(x - .5, y + height, T.item, bbox = {"boxstyle": "circle", "facecolor": "white", "edgecolor": "black"})#this line drawsa circle at the desired point and draws the T item in said circle
        if T.left is not None:#continue to the methods that draw the lines and the recursive call as long as T.left is not None
            p = np.array([[x-deltaX,y],[x, y+height]])
            draw_triangle(ax, 1, p,.9)
            draw_tree(T.left , x-deltaX, y-height, height, deltaX/2)
        if T.right is not None:#continue to the methods that draw the lines and the recursive call as long as T.right is not None
            p = np.array([[x, y+height],[x+deltaX,y]])
            draw_triangle(ax, 1, p,.9)
            draw_tree(T.right , x+deltaX, y-height, height, deltaX/2)


#lines 170 - 173 create the BST
T = None
A = [10, 4, 15, 2, 8, 12, 18, 1, 3, 5, 9, 7]
for a in A:
    T = Insert(T,a)

#call to draw_tree which is question 1
draw_tree(T, 10, 10, 10, 10)

#method call to findIterative which is question 2
print(findIterative(T, 8).item)

#method call to LtoT which is question 3
L = [1,2,3,4,5]#sample list
NEWTREE = LtoT(L)
#draw_tree(NEWTREE, 10, 10, 10, 10) #prints the tree as proof method works

#method call to TtoL which is question 4
NEWLIST = TtoL(T)
print(TtoL(T)) #prints the list to prove method works

#method call to printAtDepth2 which is question 5
printAtDepth2(T, 5)