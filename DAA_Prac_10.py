class Landscape:

    def __init__(self,row,col,matrix):
        self.Row=row
        self.Col=col
        self.Matrix=matrix

    def DFS(self,i,j):

        if(i<0 or i>=len(self.Matrix) or j<0 or j>=len(self.Matrix[0]) or self.Matrix[i][j]!=1 ):
            return

        self.Matrix[i][j]=-1

        self.DFS(i-1,j-1)
        self.DFS(i-1,j)
        self.DFS(i-1,j+1)
        self.DFS(i,j-1)
        self.DFS(i,j+1)
        self.DFS(i+1,j-1)
        self.DFS(i+1,j)
        self.DFS(i+1,j+1)

    def countIslands(self):

        count=0
        for i in range(self.Row):
            for j in range(self.Col):
                if(self.Matrix[i][j]==1):
                    self.DFS(i,j)
                    count+=1

        return count

n=int(input("Enter the no. of rows: "))
m=int(input("Enter the no. of columns: "))

matrix=[]
print("\nEnter grid elements row-wise ('0' for water and '1' for land): ")

for i in range(n):
    print(f"Row {i+1}: ")
    row=[]
    for j in range(m):
        row.    append(int(input()))
    matrix.append(row)
    print()

print("\nLandscape ('0' for water and '1' for land) is: ")
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=" ")
    print()

islands=Landscape(n,m,matrix)

print("\nTotal Number of islands is: ",islands.countIslands())