#Jon Munoz
#CS2302 Data Structures
#Lab 7
#Instructor:Olac Fuentes
#TA:Anindita Nath
#Last Modified 4/29/19

import queue 
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import datetime


#this method is the method that prints the path to a desired cell
def printPath(prev, v):
    if prev[v] != -1:#keep going untill prev[v] is -1 since that will be the beginning
        printPath(prev, prev[v])#make recursive call
        print(" --- ", end = ' ')#print the path
    print(v, end = ' ')#print the beginning cell
    
#BFS method
def breadth_first_search(G, v):
    visited = [False for i in range(len(G))]#make a list filled with False
    prev = [-1 for i in range(len(G))]#make a list filled with -1
    Q = queue.Queue()#create an empty queue
    Q.put(v)#add v into the queue
    visited[v] = True#make the visited index at v True
    while Q.empty() == False:#while loop will keep going until the queue is not empty
        u = Q.get()#extract the first item in the queue
        for t in G[u]:#go through G
            if visited[t] == False:#if visited at t is False then make it true and change prev at t to u 
                visited[t] = True
                prev[t] = u
                Q.put(t)#put t into the queue
    return prev#return the prev list

#DFS using stack method
def DFSStacks(G, v):
    visited = [False for i in range(len(G))]#make a list filled with False
    prev = [-1 for i in range(len(G))]#make a list filled with -1
    S = []#create an empty list/stack
    S.append(v)#add v to the stack
    visited[v] = True#set visited at v to True
    while len(S) != 0:#keep popping until S is empty
        u = S.pop()
        for t in G[u]:
            if visited[t] == False:#if visited at t is False then make it true and change prev at t to u 
                visited[t] = True
                prev[t] = u
                S.append(t)#add t
    return prev#return prev list

#DFS recursive method
def DFSRecursive(G, source):
    global visited#make visited global so its not constantly reset
    global prev#make prev global so its not constantly reset
    visited[source] = True#set visited at source to True
    for t in G[source]:#go through G
        if visited[t] == False:#if visited at t is False then make it true
            prev[t] = source#make prev at t equal to source
            DFSRecursive(G, t)#recursive call
    return prev#return prev list
        
def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)


def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w
###########################################################################

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

#finds the root of a given number i
def find(S,i):
    if S[i]<0:#if S[i] < zero then youre at the root return i
        return i
    return find(S,S[i])#recursive call if S[i] is not less that 0

#finds the root of a given number i using path compression
def findC(S,i):
    if S[i] < 0:#if S[i] < zero then youre at the root return i
        return i
    root = findC(S,S[i])#recursively get to the root
    S[i] = root#directly set the root of i to the root value
    return root
        
#combines the two given values using their size to choose who get combined
def unionbySize(S,i,j):
    ri = findC(S,i)#find the root of the first value
    rj = findC(S,j)#find the root of the second value
    if ri!=rj:#if the roots are not the same then you complete the union
        if S[ri] > S[rj]:#if S[ri] is greater than S[rj] then you combine S[rj] to S[ri] 
            S[rj] += S[ri]
            S[ri] = rj
        else:#rif S[rj] is greater than S[ri] then you combine S[ri] to S[rj] 
            S[ri]+=S[rj]
            S[rj] = ri
            
#counts the number of sets in the given disjoint set forest
def NumSets(S):
    count = 0#counter
    for i in range(len(S)):#traverse the entire DSF
        if S[i] < 0:#if an value is less than 0 then add one to the counter
            count += 1
    return count

#union the two given values
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j) 
    if ri!=rj: # Do nothing if i and j belong to the same set 
        S[rj] = ri
        
#def buildAdjacencyList(:)
        
def draw_graph(G):
    fig, ax = plt.subplots()
    n = len(G)
    r = 30
    coords =[]
    for i in range(n):
        theta = 2*math.pi*i/n+.001 # Add small constant to avoid drawing horizontal lines, which matplotlib doesn't do very well
        coords.append([-r*np.cos(theta),r*np.sin(theta)])
    for i in range(n):
        for dest in G[i]:
            ax.plot([coords[i][0],coords[dest][0]],[coords[i][1],coords[dest][1]],
                     linewidth=1,color='k')
    for i in range(n):
        ax.text(coords[i][0],coords[i][1],str(i), size=10,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.set_aspect(1.0)
    ax.axis('off') 

#THis method converts the walls list to an Adjacency Listin order to do graph functions
def ToaJ(walls, originalWall, numCells):
    AL = []#Adjacency List
    for k in range(numCells):#fill the list with empty cells
        AL.append([])
    for i in range(len(originalWall)):#go through the entire original walls list
        if originalWall[i] not in walls:#if a wall is in the original walls list but not the list once the graph is made then the cells are connected
            AL[originalWall[i][0]].append(originalWall[i][1])#add to adjacency list
            AL[originalWall[i][1]].append(originalWall[i][0])#add to adjacency list
    return AL#return the adjacency list

plt.close("all")
ans1 = input("How many rows would you like?  ")#this line gets the user input for the desired number of rows
print("Number of rows:", ans1)
rows = int(ans1)#parse the input to an int
ans2 = input("How many columns would you like? ")#this line gets the user input for the desired number of columns
print("Number of columns:", ans2)
columns = int(ans2)#parse the input to an int

maze_rows = rows#set maze_rows to the value of rows
maze_cols = columns#set maze_cols to the value of columns

n = rows * columns#used to tell how many cells there are

print()
print("There are ", n, "cells in the maze")
m = input("How many walls do you want to remove?")
m = int(m)

original = wall_list(maze_rows,maze_cols)#store the original walls list into a variable for comparisons later
walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 

S = DisjointSetForest(maze_rows * maze_cols)#create a DSF with the size of the value of rows times the value of columns

if m < n - 1:
    print("A path from source to destination is not guaranteed to exist")
    while m != 0:#keep doing the below code until there is only one set
        w = random.choice(walls)#set w to a random list within the bigger list
        ind = walls.index(w)#get the index of the chosen list w
        if findC(S,w[0]) != findC(S,w[1]):#find the parents of the number in index 0 and 1 of the list using path compression and if they are different union them
            walls.pop(ind)#pop the wall connecting the two numbers since we want to "union" them
            unionbySize(S,w[0],w[1])#use unionbySize method to connect the two values within the DSF
            m -= 1#one set is removed so subtract 1 from the numberOfSets value
    draw_maze(walls,maze_rows,maze_cols)#draw the new maze
    
if m == n - 1:
    print("The is a unique path from source to destination")
    while m != 0:#keep doing the below code until there is only one set
        w = random.choice(walls)#set w to a random list within the bigger list
        ind = walls.index(w)#get the index of the chosen list w
        if findC(S,w[0]) != findC(S,w[1]):#find the parents of the number in index 0 and 1 of the list using path compression and if they are different union them
            walls.pop(ind)#pop the wall connecting the two numbers since we want to "union" them
            unionbySize(S,w[0],w[1])#use unionbySize method to connect the two values within the DSF
            m -= 1#one set is removed so subtract 1 from the numberOfSets value
    draw_maze(walls,maze_rows,maze_cols)#draw the new mazee
    
if m > n - 1:
    print("There is at least one path from source to destination")
    numberOfSets = NumSets(S)
    while m != 0:#keep doing the below code until there is only one set
        w = random.choice(walls)#set w to a random list within the bigger list
        ind = walls.index(w)#get the index of the chosen list w
        if findC(S,w[0]) != findC(S,w[1]):#find the parents of the number in index 0 and 1 of the list using path compression and if they are different union them
            walls.pop(ind)#pop the wall connecting the two numbers since we want to "union" them
            unionbySize(S,w[0],w[1])#use unionbySize method to connect the two values within the DSF
            numberOfSets -= 1
            m -= 1#one set is removed so subtract 1 from the numberOfSets value
        if numberOfSets == 1 and m > 0:
            walls.pop(ind)
            m -= 1
    draw_maze(walls,maze_rows,maze_cols)#draw the new maze
    
numCells = maze_rows * maze_cols#numCells variable helps when doing the printpath call
    

#below are the calls to the differant search methods and rhe paths that they produce 
print("------------------------------------")
print("ADJACENCY LIST")
G = ToaJ(walls, original, numCells)
visited = [False for i in range(len(G))]
prev = [-1 for i in range(len(G))]
print(ToaJ(walls, original, numCells))
print()
print("BFS")
start = datetime.datetime.now()#start time of maze construction
K = breadth_first_search(G, 0)
end = datetime.datetime.now()#end time of creating the maze
elapsed = end - start#total time  
print(elapsed)
print(K)
printPath(K, numCells - 1)
print()
print("------------------------------------")
print("DFS with Stack")
start = datetime.datetime.now()#start time of maze construction
J = DFSStacks(G,0)
end = datetime.datetime.now()#end time of creating the maze
elapsed = end - start#total time  
print(elapsed)
print(J)
printPath(J, numCells - 1)
print()
print("------------------------------------")
print("DFS Recursive")
start = datetime.datetime.now()#start time of maze construction
H = DFSRecursive(G,0)
end = datetime.datetime.now()#end time of creating the maze
elapsed = end - start#total time 
print(elapsed) 
print(H)
printPath(H, numCells - 1)