def MinOperations(str1,str2,m,n):

    if m==0:
        return n
    if n==0:
        return m

    if str1[m-1]==str2[n-1]:
        return MinOperations(str1,str2,m-1,n-1)

    return 1 + min(MinOperations(str1,str2,m,n-1),
                   MinOperations(str1,str2,m-1,n),
                   MinOperations(str1,str2,m-1,n-1))

str1=input("Enter first string: ")
str2=input("Enter second string: ")
len1=len(str1)
len2=len(str2)

print(f"\nFor conversion of {str1} to {str2}; ")
print("\nMinimum no. of operations required: ",MinOperations(str1,str2,len1,len2))
