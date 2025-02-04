class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[-1][-1]

m=int(input("Enter the rows of matrix: "))
n=int(input("Enter the columns of matrix: "))

s=Solution.uniquePaths(m,n)
print(s)