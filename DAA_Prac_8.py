# Do not consider this code
from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)

    def addEdge(self,v,e):
        self.graph[v].append(e)
        self.graph[e].append(v)

    def isCyclicUtil(self,v,visited,parent):
        visited[v]=True

        for i in self.graph[v]:
            if (visited[i]==False):
                if(self.isCyclicUtil(i,visited,v)):
                    return True
            elif(parent!=i):
                    return True

        return False

    def isCyclic(self):

        visited = [False]*(self.V)

        for i in range(self.V):
            if(visited[i]==False):
                if(self.isCyclicUtil(i,visited,-1)==True):
                    return True

        return False


vertices=int(input("Enter the number of vertices: "))
edges=int(input("Enter the number of edges: "))

g=Graph(vertices)
print("\nEnter the edges in format (vertex1 vertex2): ")
for i in range(0,edges):
    vertice1,vertice2=input().split(" ")
    if(0<=int(vertice1)<vertices and 0<=int(vertice2)<vertices):
        g.addEdge(vertice1,vertice2)
    else:
        print("\nEnter correct vertice number for the edge")

if(g.isCyclic()):
    print("\nGraph contain cycle")
else:
    print("\nGraph doesn't contain cycle")