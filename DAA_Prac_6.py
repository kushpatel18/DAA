def FindDuplicate(arr,n):

    for i in arr:
        temp=i
        if(arr.count(temp)!=1):
            return temp
        else:
            continue

    return -1

n=int(input("Enter the length of array: "))
arr=[]

print("\nEnter the elements for the array: ")
for i in range(0,n):
    arr.append(int(input("Enter element: ")))

flag=FindDuplicate(arr,n)

if(flag==-1):
    print("\nNo Duplicate Values are present in the array")
else:
    print("\nDuplicate Value is: ",flag)