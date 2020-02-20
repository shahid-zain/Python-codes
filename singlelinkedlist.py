class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class singlell:
    def __init__(self):
        self.head=None

    def insert(self):
        if self.head==None:
            node1=node(int(input("enter the value : ")))
            self.head=node1
        else:
            pos=int(input("enter the position : "))
            new=node(int(input("enter the value : ")))
            temp=self.head
            for i in range(pos-1):
                temp=temp.next
            new.next=temp.next
            temp.next=new

    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
obj=singlell()
while(True):
    n=int(input("1.insert 2.traverse :"))
    if n==1:
        obj.insert()
    elif n==2:
        obj.traverse()
    else:
        exit(0)