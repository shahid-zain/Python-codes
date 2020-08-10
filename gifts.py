def distribute(lst):
    total=1
    for i in range(1,len(lst)):
        if lst[i]>lst[i-1]:
            total+=2
        else:
            total+=1
        
    return total

cases=int(input())
lst=[]
for i in range(cases):
    n=int(input())
    lst=list(map(int,input().split()))[:n]
    total=1
    for i in range(1,len(lst)):
        if lst[i]>lst[i-1]:
            total+=2
        else:
            total+=1
    print(total)