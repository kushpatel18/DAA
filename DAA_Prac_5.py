def Platforms(n,arr,dep):
    count=1
    for i in range(1,n):
        arr_time=arr[i]
        dep_time=dep[i-1]
        arr_hour,arr_min=[int(j) for j in arr_time.split(":")]
        dep_hour,dep_min=[int(k) for k in dep_time.split(":")]

        if(arr_hour<dep_hour):
            count+=1
        elif(arr_hour==dep_hour):
            if(arr_min<=dep_min):
                count+=1
        else:
            continue

    return count
trains=int(input("Enter the no. of trains: "))
arrival=[]
departure=[]

print("\nEnter arrival time for trains in HH:MM")
for i in range(0,trains):
    temp=input(f"Train {i+1}: ")
    arrival.append(temp)

print("\nEnter departure time for trains in HH:MM")
for i in range(0,trains):
    temp=input(f"Train {i+1}: ")
    departure.append(temp)

print("\nMinimum no. of platforms needed: ",Platforms(trains,arrival,departure))
