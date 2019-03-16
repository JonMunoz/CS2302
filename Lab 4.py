#Jon Munoz
#CS2302 Data Structures
#Lab 4
#Instructor:Olac Fuentes
#TA:Anindita Nath, Maliheh Zargaran
#Last Modified 3/15/19

# Code to implement a B-tree 
# Programmed by Olac Fuentes
# Last modified February 28, 2019

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
#####################################################
        
#this method will find the height of a given B-Tree
def height(T):
    if T.isLeaf:#if the current node is a you want to return 0
        return 0
    return 1 + height(T.child[0])#if the node is not a leaf then you want to add 1 to the height value

#Dthis method converts a B-Tree to a sorted list
def TtoL(T):
    if T.isLeaf:#when the node is a leaf you want to return a list
        List = list(T.item)#the returned list is a list of the current node
        return List
    else:
        L = []#create an empty list to add to
        for i in range(len(T.item)):#for loop will populate two differant arrays L1 and L2
            L1 = TtoL(T.child[i])#L1 is filled with each child node
            L2 = [T.item[i]]#L2 is populated with each item node
            L = L + L1 + L2#L is then made to be the concatination of L,L1, and L2
        L4 = TtoL(T.child[-1])#L4 must be called with the last child node since the for loop does not go to it
    return L + L4#add L4 to the rest of the created list


#this method goes to a given depth and returns the smallest number at that depth
def SmallestAtDepth(T, d):
    if T == None:#if T is none then the item was not found and return none
        return None
    if d == 0:#if d is 0 then you are at your desired depth
        return T.item[0]#return the furthest left element
    return SmallestAtDepth(T.child[0], d - 1)#call the method recursively with the leftmost child

#this method goes to a given depth and returns the largest number at that depth
def LargestAtDepth(T, d):
    if T == None:#if T is none then the item was not found and return none
        return None
    if d == 0:#if d is 0 then you are at your desired depth
        return T.item[len(T.item) - 1]#return the furthest right element
    return LargestAtDepth(T.child[len(T.item)], d - 1)#call the method recursively with the rightmost child

    
#this method returns the number of nodes at a given depth
def NodesAtDepth(T, d):
    if T is None:#if T is none then there is no node and you return 0
        return 0
    if d == 0:#if d is 0 then you are at the desired depth so you return 1
        return 1
    else:
        num = 0#num is the total number of nodes (which is initially 0)
        for i in range(len(T.child)):#for loop goes to all children
            if T.child != None:
                num += NodesAtDepth(T.child[i], d - 1)#if the child is not none then you want to call the method recursively with each child
    return num#return the total
           
#this method prints all the items at a given depth
def PrintAtDepthD(T, d):
    if d > height(T):#if the given depth is larger than the height of the tree then there are no nodes
        print("No nodes at this depth")#print that there are no nodes
        return
    if d == 0:#if d is 0 then you are at the desired depth so you print all the items
        for i in range(len(T.item)):#for loop prints all items
            print(T.item[i], end = ' ')
    else:
        for i in range(len(T.child)):#for loop goes through every child
            PrintAtDepthD(T.child[i], d - 1)
            
#this method gets the total number of nodes in the tree that are full and returns the value
def FullNodes(T):
    if len(T.item) == T.max_items:#if the length of a given node is equal the max_items value then it is full so return 1
        return 1
    else:
        total = 0#total keeps track of the total number of full nodes
        for i in range(len(T.child)):#for loop goes through every child node
            total = total + FullNodes(T.child[i])#add to total
        return total

#this method will find the total number of leaf nodes that are full
def FullLeafNodes(T):
    if T.isLeaf and len(T.item) == T.max_items:#if a node is a leaf and is full then you want to return 1
        return 1
    else:
        total = 0#total keeps track of the total number of full leaf nodes
        for i in range(len(T.child)):#for loop goes through every child node
            total = total + FullLeafNodes(T.child[i])#add to total
        return total

#this method will find a given number if it is in the tree and return its depth
def FindDepth(T, k):
    if k in T.item:#if the key is in the current node then you return 0
        return 0
    depth = 0#depth initially initialized to 0
    if k > T.item[len(T.item)-1]:#if the key is greater than the last item go to last child
        depth = FindDepth(T.child[len(T.item)], k)
    elif k < T.item[0]:#if key is less than the first item travel to the leftmost child
        depth = FindDepth(T.child[0], k)
    if depth >= 0:#if depth is greater than or equal to 0 add 1 to depth 
        return 1 + depth
    else:
        return -1#if the key is not found return -1
            
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6,7,8,9,201,202,21,24,22,23]
T = BTree()    
for i in L:
    #print('Inserting',i)
    Insert(T,i)
    #PrintD(T,'') 
    #Print(T)
    #print('\n####################################')
          
PrintD(T, '')
print('\n####################################')

#Below are the method calls
print(height(T))
print(TtoL(T))
print("Smallest element at given depth:", SmallestAtDepth(T, 1))
print("Largest element at given depth:", LargestAtDepth(T, 1))
print(NodesAtDepth(T,2))
PrintAtDepthD(T, 1)
print()
print(FullNodes(T))
print(FullLeafNodes(T))
print(FindDepth(T, 70))