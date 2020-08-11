def distribute(lst):
    total=1
    for i in range(1,len(lst)):
        if lst[i]>lst[i-1]:
            total+=2
        else:
            total+=1
        
    return total

'''cases=int(input())
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
    print(total) '''

def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]

        mergesort(l)
        mergesort(r)

        i=j=k=0

        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1

        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1


arr=[14,46,43,27,57,41,45,21,70]
mergesort(arr)
print(arr)