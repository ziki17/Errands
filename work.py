import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


#The following function returns a random graph on nodes
#1,...,N where edges are chosen with equal probability
#The graph is returned as a dictionary keyed by the
#The corresponding values are sorted lists of adjacent nodes

def randGraph(N):
    #initialize G:
    G = {1:[1]}
    for i in range(2,N):
        G[i] = []
    #iterate through potential edges:
    for i in range(2,N):
        a = random.randint(1,i-1)
        G[i].append(a)
    #sort adjacency lists before returning:
    for i in G:
        G[i].sort()
    return G

def randGraphWithProbability(N):
    #initialize G:
    G = {1:[1]}
    for i in range(2,N):
        G[i] = []
    #iterate through potential edges:
    for i in range(2,N):
        a = probabilityNodes(G,1,i)
        G[i].append(a)
    #sort adjacency lists before returning:
    for i in G:
        G[i].sort()
    return G
#The following function returns all the degrees of the graph
def findAllDegrees(G):
    all_degrees = map(len, G.values())
    return all_degrees
#The following function returns the adjacency Matrix of the graph
def adjacenyMatrix(adjacencyList):
    return [[1 if x == y else 0 for x in adjacencyList] for y in adjacencyList]
#The follwing function returns the In and Out along with combined degree of each node
# It is returned as three lists.
def getInOutDegreesnj(G,nj):
    inDegreeList = {}
    outDegreeList = {}
    combinedDegreeList = {}
    for i in G:
        inDegreeList[i] = 0
        outDegreeList[i] = 0
        combinedDegreeList[i] = 0
    for j in range(1,nj):
        cd = G[j][0]
        inDegreeList[cd] += 1
        outDegreeList[i] += 1
        combinedDegreeList[i] += 1
        combinedDegreeList[cd] +=1
    return inDegreeList,outDegreeList, combinedDegreeList

def getInOutDegrees(G):
    inDegreeList = {}
    outDegreeList = {}
    combinedDegreeList = {}
    for i in G:
        inDegreeList[i] = 0
        outDegreeList[i] = 0
        combinedDegreeList[i] = 0
    for i in G:
        cd = G[i][0]
        inDegreeList[cd] += 1
        outDegreeList[i] += 1
        combinedDegreeList[i] += 1
        combinedDegreeList[cd] +=1
    return inDegreeList,outDegreeList, combinedDegreeList

def probabilityNodes(G,start,end):
    i, o, c = getInOutDegreesnj(G,end)
    arre = range(start, end)
    for key in c:
        total_nodes = key +1
    p = [float(key)/(total_nodes+1) for x, key in c.iteritems()]
    print p
    return np.random.choice(arre,1,p)[0] # Return the random node generated from the loop
    #return p
def main():
    randomGraphProb = randGraphWithProbability(4) # We get the random graph where t =1000 as mentioned in Task1
    print randomGraphProb
    inDegreeP,outDegreeP,CombinedDegreeP = getInOutDegrees(randomGraphProb)
    print CombinedDegreeP
    plt.bar(CombinedDegreeP.keys(), CombinedDegreeP.values(), color='g')
    plt.show()
    #plt.bar(CombinedDegree.keys(), CombinedDegree.values(), color='g')
    #plt.show()

if __name__ == "__main__":
   main()