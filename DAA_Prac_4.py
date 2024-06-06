def isPossible(pos,dist,s,c):
    count=1
    prev=pos[0]

    for curr_pos in range(1,s):
        curr=pos[curr_pos]
        if(curr-prev>=dist):
            prev=curr
            count+=1

    if(count>=c):
        return True
    return False



stalls=int(input("Enter no. of stalls: "))
cows=int(input("Enter no. of cows: "))
pos=[]

print("\nEnter positions of the stalls: ")
for i in range(0,stalls):
    location=int(input(f"Stall {i+1}: "))
    pos.append(location)

pos.sort()

temp=-1
max_dist=pos[stalls-1]

for dist in range(1,max_dist+1):
    if(isPossible(pos,dist,stalls,cows)):
        ans=dist
    else:
        break

print("\nLargest minimum distance between two stalls: ",ans)