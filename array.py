class arrays:
    def __init__(self,size):
        self.array=[0]*size

    def insert(self,pos):
        if self.array[pos]==0:
            self.array[pos]=int(input("enter the value : "))
        else:
            print("already value existed")

    def traverse(self):
        for i in range(len(self.array)):
            print(self.array[i],end=" ")

    def delete(self,pos):
        if self.array[pos]!=0:
            self.array[pos]=0
        else:
            print("already empty...")

size=int(input("enter the size of array :"))
arr=arrays(size)
while(True):
    n=int(input("\n 1.insert 2.delete 3.traverse 4.exit \n enter your choice : "))
    if n==1:
        pos=int(input("enter the position to insert : "))
        arr.insert(pos)
    elif n==2:
        pos = int(input("enter the position to insert : "))
        arr.delete(pos)
    elif n==3:
        arr.traverse()
    elif n==4:
        exit(0)
    else:
        exit(0)