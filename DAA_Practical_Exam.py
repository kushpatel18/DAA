def LinearSearch(arr,n):
    flag=0
    for i in range(0,len(arr)):
        temp=arr[i]
        if(temp==n):
            flag=1
            break

    if(flag==1):
        print(f"Target value {n} is present at index {i} ")
    else:
        arr.append(n)
        arr.sort()
        print(f"Target value {n} is not present but can be inserted at index {arr.index(n)}")


arr=[]
size=int(input("Enter the size of array: "))

print("\nEnter elements in acending order: ")
for i in range(0,size):
    ele=int(input("Enter element: "))
    arr.append(ele)

arr.sort()
print("\nSorted Array: ",arr)

target=int(input("\nEnter the target value: "))
LinearSearch(arr,target)


