#Jon Munoz
#CS2302 Data Structures
#Lab 8
#Instructor:Olac Fuentes
#TA:Anindita Nath
#Last Modified 5/9/19

import random
import numpy as np
from math import *
import math
import datetime

#this method compares two trig functions together and sees if they are similar or not
def discovery(L,tries = 1000,tolerence = 0.0001):
    TF = []#TF is the list where I store the results of my comarisons
    for b in range(len(L)):#this for loop fills TF with empty list equal to the number of trig functions that are in the passed list
        TF.append([])
    for i in range(len(L)):#this for loop goes through each index in TF one by one in order to store results at the correct index
        val = True#set val equal to True since before comparisons it should be True
        for j in range(len(L)):#this for loop gooes through the entire list comparing each index j to index i 
            val = True#set val equal to True since before comparisons it should be True
            for k in range(tries):#for loop does 1000 runs to see if the two functions are similar
                t = random.uniform(-math.pi,math.pi)#gets a random number between -pi and pi
                y1 = eval(L[i])
                y2 = eval(L[j])
                if np.abs(y1 - y2) > tolerence:#if the difference is greater than the sum then the two functions are not similar so set val to False
                    val = False
            TF[i].append(val)#append val to the results list
    return TF#return the TF list once all comparisons are done

#this method is the actual backtracking part of the subsets method
def subsets2(S,last,goal):
    if goal == 0:#if goal is 0 then you return just an empty list
        return []
    if goal<0 or last<0:#if goal or last value is less that 0 return an empty list
        return []
    subset = []#create a list subset to store results 
    if S[last] > goal:#if the value at index last is greater than goal then you obviously cant take it 
        return subsets2(S, last - 1, goal) #dont take S[last]
    else:
        subset.append(S[last])#add S[last] to the subset list
        return subsets2(S,last-1,goal - S[last]) + subset #take S[last]

#this method does the basic preliminary checks to see if its even possible to get two equal subsets
def subsets(S,index):
    sumList = 0#holds the sum of the passed list S
    for i in range(len(S)):#for loop goes through entire list and adds it to sum
        sumList += S[i]
    if sumList % 2 != 0:#if the sum of the original list is not even then it is not possible to get two subsets to have equal value so return False immediately
        return False
    NL = subsets2(S,index,sumList//2)#call subsets2 in order to get one of the subsets of S
    sumNL = 0#sumNL will hold the sum of 
    sumOtherHalf = 0#holds the sum of the other sublist not returned by the method
    otherHalf = []#other list that wasnt returned
    for j in range(len(S)):#fills otherHalf with elements not in NL
        if S[j] not in NL:
            otherHalf.append(S[j])
    for i in range(len(NL)):#gets the sum of NL
        sumNL += NL[i]
    for g in range(len(otherHalf)):#gets the sum of the other list
        sumOtherHalf += otherHalf[g]
    if sumNL == sumList//2 and sumOtherHalf == sumList//2:#if the two list equal to half the original then print the list 
        print(NL, otherHalf)
    else:
        print("No sublist exist")#else printno such sublist exists
        
#below are all the added functions
f1 = 'sin(t)'
f2 = 'cos(t)'
f3 = 'tan(t)'
f4 = '1/cos(t)'#put sec as i/cos since sec was not available and these two are equivalent
f5 = '-sin(t)'
f6 = '-cos(t)'
f7 = '-tan(t)'
f8 = 'sin(-t)'
f9 = 'cos(-t)'
f10 = 'tan(-t)'
f11 = 'sin(t)/cos(t)'
f12 = '2*sin(t/2)*2*cos(t/2)'
f13 = 'sin(t)**2'
f14 = '1-cos(t)**2'
f15 = '(1-cos(2*t))/2'
f16 = '1/cos(t)'
#f17 = 'sin(t)'

#append all functions to a list
functions = []
functions.append(f1)
functions.append(f2)
functions.append(f3)
functions.append(f4)
functions.append(f5)
functions.append(f6)
functions.append(f7)
functions.append(f8)
functions.append(f9)
functions.append(f10)
functions.append(f11)
functions.append(f12)
functions.append(f13)
functions.append(f14)
functions.append(f15)
functions.append(f16)
#functions.append(f17)
#print(functions)
#    
#start = datetime.datetime.now()
#result = discovery(functions)
#end = datetime.datetime.now()
#elapsed = end - start
#print(elapsed)
#
#print(result)

#test list for subsets
test = [2, 4, 5, 9]

start = datetime.datetime.now()
subsets(test,len(test) - 1)
end = datetime.datetime.now()
elapsed = end - start
print(elapsed)