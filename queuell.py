class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queuell:
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self):
        new=node(int(input("enter the value : ")))
        if self.head==None and self.tail==None:
            self.head=new
            self.tail=new
            print("1st node is inserted")
        else:
            self.tail.next=new
            self.tail=new
            print("node is inserted at tail")

    def dequeue(self):
        if self.head==None:
            print("queue is empty..")
        else:
            self.head=self.head.next
            print("node is deleted ")

    def peek(self):
        if self.head==None:
            print("queue is empty..")
        else:
            print(self.head.value)

obj=Queuell()
while True:
    n=int(input("1.enqueue 2.dequeue 3.peek 4.exit  : "))
    if n==1:
        obj.enqueue()
    elif n==2:
        obj.dequeue()
    elif n==3:
        obj.peek()
    else:
        exit(0)