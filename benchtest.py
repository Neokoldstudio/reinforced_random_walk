"""
Created on Tue Jan 10 19:50:25 2023
"""

import random
import matplotlib.pyplot as plt
import numpy as np

Yn=[0] #Number of times path alpha was chosen
Ynovern=[0] #Asymptotic behaviour of Yn
Zn=[0] #Number of times path beta was chosen
Znovern=[0] #Asymptotic behaviour of Zn

NYn=[]
NZn=[]
NYnovern=[]
NZnovern=[]

avYn=[] #average number of times path alpha was chosen
avYnovern=[] #average asymptotic behaviour of Yn
avZn=[] #average number of times path beta was chosen
avZnovern=[] #average asymptotic behaviour of Zn

X,A,B=0,1,1 #Initial definition of the [X,A,B] triplet

########### REINFORCEMENT FUNCTIONS #############

def no(x):
    return x

def linear(x):
    return x+1

def geo(x):
    return 1.1*x

reinforcementFunctions = [no, linear, geo]

#################################################

def clamp(num, min_value, max_value):
        num = max(min(num, max_value), min_value)
        return num

def average(X, Y) : #creation of Y a list of average values from X made of N lists of n values
    for i in range(0, n):
        average=0
        for j in range(0, N):
            average+=1/N*X[j][i]
        Y.append(average)


def experiment(triplet:tuple, iterations, reinforcement):

    A = triplet[1]
    B = triplet[2]

    for i in range(1, iterations+1):
        U=random.random()
        if U<=A/(A+B) :
            A=reinforcement(A)
            #update number of time for each path :
            Yn.append(Yn[i-1]+1)
            Zn.append(Zn[i-1])
            #asymptotic behaviour :
            Ynovern.append((Yn[i-1]+1)/i)
            Znovern.append((Zn[i-1])/i)
        else :
            B=reinforcement(B)
            #update number of time for each path :
            Yn.append(Yn[i-1])
            Zn.append(Zn[i-1]+1)
            #asymptotic behaviour :
            Ynovern.append((Yn[i-1])/i)
            Znovern.append((Zn[i-1]+1)/i)
    print("Yn : "+str(Yn[n]))
    print("Zn : "+str(Zn[n]))

    return (Yn, Zn, Ynovern, Znovern)


def draw(results : tuple) :
    #Graphs
    Naxis=np.linspace(0, n, n)

    f1=plt.figure(1)
    plt.plot(Naxis, results[0], color='blue', label=r'Path $\alpha$ : $Y_n(n)$')
    plt.plot(Naxis, results[1], color='red', label=r'Path $\beta$ : $Z_n(n)$')
    plt.xlabel("n")
    plt.ylabel("Number of times the path was chosen")
    plt.title("Number of times each path are chosen for "+str(N)+" experiments")
    plt.legend()
    plt.show()

    f2=plt.figure(2)
    plt.plot(Naxis, results[2], color='blue', label=r'Path $\alpha$ : $\frac{Y_n(n)}{n}$')
    plt.plot(Naxis, results[3], color='red', label=r'Path $\beta$ : $\frac{Z_n(n)}{n}$')
    plt.xlabel("n")
    plt.ylabel("Proportion")
    plt.legend()
    plt.show()

#draw(experiment((X, A, B), n, r))

if(__name__ == '__main__'):

    forceIndex = int(input("chose your reinforcement function :\n[0] : no reinforcement\n[1] : linear reinforcement\n[2] : geometric reinforcement\n>"))
    forceIndex = clamp(forceIndex,0,2)
    reinforce = reinforcementFunctions[forceIndex]

    n=int(input("n = ")) #Choice of the number of iterations
    N=int(input("N = ")) #Choice of the number of experiments

    for i in range(1, N+1) : #creating lists for N experiments
        experiment((X, A, B), n, reinforce)
        NYn.append(Yn)
        Yn=[0]
        NZn.append(Zn)
        Zn=[0]
        NYnovern.append(Ynovern)
        Ynovern=[0]
        NZnovern.append(Znovern)
        Znovern=[0]
    average(NYn, avYn), average(NZn, avZn), average(NYnovern, avYnovern), average(NZnovern, avZnovern) #computing the averages

    draw((avYn, avZn, avYnovern, avZnovern))