import random
import matplotlib.pyplot as plt
import numpy as np
Yn=[0] #Number of times path alpha was chosen
Ynovern=[0] #Asymptotic behaviour of Yn
Zn=[0] #Number of times path beta was chosen
Znovern=[0] #Asymptotic behaviour of Zn

X,A,B=0,1,1 #Initial definition of the [X,A,B] triplet

def r(x): #Definition of the reinforcement function
    return x

n=int(input("n = ")) #Choice of the number of iterations

def experience(triplet:tuple, iterations, reinforcement):

    A = triplet[1]
    B = triplet[2]

    for i in range(1, iterations+1):
        U=random.random()
        if U<=A/(A+B) :
            A=r(A)
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
    N=np.linspace(0, n, n+1)

    f1=plt.figure(1)
    plt.plot(N, results[0], color='blue', label=r'Path $\alpha$ : $Y_n(n)$')
    plt.plot(N, results[1], color='red', label=r'Path $\beta$ : $Z_n(n)$')
    plt.xlabel("n")
    plt.ylabel("Number of times the path was chosen")
    plt.title("Number of times each path are chosen")
    plt.legend()
    plt.show()

    f2=plt.figure(2)
    plt.plot(N, results[2], color='blue', label=r'Path $\alpha$ : $\frac{Y_n(n)}{n}$')
    plt.plot(N, results[3], color='red', label=r'Path $\beta$ : $\frac{Z_n(n)}{n}$')
    plt.xlabel("n")
    plt.legend()
    plt.show()

draw(experience((X, A, B), n, r))