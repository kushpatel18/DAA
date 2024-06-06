def RepeatingAndMissing(arr,n):
    repeating=-1
    missing=-1
    arr2=[]

    for i in arr:
        if(arr.count(i)>1):
            repeating= i
        else:
            continue

    for i in range(1,n+1):
        arr2.append(i)

    for i in arr2:
        if(i not in arr):
            missing=i
        else:
            continue


    if(repeating==-1):
        print("\nThere are no repeating elements")
    else:
        print("\nRepeating Element: ",repeating)

    if(missing==-1):
        print("\nThere are no missing elements")
    else:
        print("\nMissing Element: ",missing)

n=int(input("Enter the length of array: "))
arr=[]

print("\nEnter integer elements for the array:")
for i in range(0,n):
    temp=int(input("Enter element: "))
    arr.append(temp)

RepeatingAndMissing(arr,n)

