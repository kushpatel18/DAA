def removeKdigits(num,k):

    n=len(num)
    stack=[]

    for digit in num:
        while(len(stack)>0 and k>0 and ord(stack[len(stack)-1])>ord(digit)):
            stack.pop()
            k -=1
        if(len(stack)>0 or digit!='0'):
            stack.append(digit)

    while len(stack)>0 and k:
        stack.pop()
        k -=1

    if (len(stack)==0):
        return '0'

    num=list(num)
    while(len(stack)>0):
        num[n-1]=stack[len(stack)-1]
        stack.pop()
        n-=1
    return "".join(num[n:])

str1=input("Enter a number: ")
k=int(input("Enter the no. of digits you want to remove: "))

print(f"\nSmallest Possible Integer after removing {k} digits: ",removeKdigits(str1,k))

