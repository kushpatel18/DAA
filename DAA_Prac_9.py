# Do not consider this code
from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.edges=defaultdict(list)
        self.visited=[False for i in range(n)]
        self.bridges=[]
        self.low=[float('inf') for i in range(n)]
        self.disc=[float('inf') for i in range(n)]

    def add_edge(self,u,v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def bridge(self,vertex,time,parent):
        self.low[vertex]=time
        self.disc[vertex]=time
        self.visited[vertex]=True
        min_child_low=float('inf')


        time+=1


        flag=0
        for i in range(len(self.edges[vertex])):
            if self.edges[vertex][i]!=parent:
                flag=1
                if(self.visited[self.edges[vertex][i]]):
                    child_low=self.low[self.edges[vertex][i]]
                    if child_low>self.disc[vertex]:
                        self.bridges.append([vertex,self.edges[vertex][i]])
                    min_child_low=min(min_child_low,child_low)


                else:

                    child_low=self.bridge(self.edges[vertex][i],time,vertex)
                    if child_low>self.disc[vertex]:
                        self.bridges.append([vertex,self.edges[vertex][i]])

                    min_child_low=min(min_child_low,child_low)



        if flag==0:
            return self.low[vertex]

        self.low[vertex]=min_child_low
        return self.low[vertex]



class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g=Graph(n)
        for i in range(len(connections)):
            g.add_edge(connections[i][0],connections[i][1])
        if len(connections)==0:
            return []
        g.bridge(connections[0][0],0,None)
        return g.bridges

s=Solution.criticalConnections(1,[(1,2),(2,3),(3,1),(0,2)])
print(s)