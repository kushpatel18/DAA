def FreshOranges(i,j):

    if(i>=0 and i<n and j>=0 and j<m):
        return True
    return False

def RottenOranges(mat):

    changed=False
    no=2
    while(True):
        for i in range(n):
            for j in range(m):

                if(mat[i][j]==no):
                    if(FreshOranges(i+1,j) and mat[i+1][j]==1):
                        mat[i+1][j]=mat[i][j] +1
                        changed=True

                    if(FreshOranges(i,j+1) and mat[i][j+1]==1):
                        mat[i][j+1]=mat[i][j] +1
                        changed=True

                    if(FreshOranges(i-1,j) and mat[i-1][j]==1):
                        mat[i-1][j]=mat[i][j] +1
                        changed=True

                    if(FreshOranges(i,j-1) and mat[i][j-1]==1):
                        mat[i][j-1]=mat[i][j] +1
                        changed=True

        if(not changed):
            break
        changed=False
        no+=1

    for i in range(n):
        for j in range(m):
            if(mat[i][j]==1):
                return -1

    return no-2


n=int(input("Enter the no. of rows: "))
m=int(input("Enter the no. of columns: "))

matrix=[]
print("\nEnter grid elements ('0' for empty cell, '1' for fresh orange and '2' for rotten orange): ")

for i in range(n):
    print(f"Row {i+1}: ")
    row=[]
    for j in range(m):
        row.    append(int(input()))
    matrix.append(row)
    print()

print("\nOranges are placed ('0' for empty cell, '1' for fresh orange and '2' for rotten orange) as: ")
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=" ")
    print()
print("\nMinimum time required for all oranges to rot: ",RottenOranges(matrix))

