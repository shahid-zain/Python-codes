class node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None
    
class ll:
    def __init__(self):
        self.head=None
    
    def insert(self,head,value):
        if head==None:
            head=node(value)
        else:
            head.next=self.insert(head.next,value)
            head.next.prev=head
        return head
    
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def reverse(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data)
            temp=temp.prev

    def delete(self,head,value):
        if head.data==value:
            return head.next
        else:
            head.next=self.delete(head.next,value)
            head.next.prev=head
        return head

obj=ll()
while True:
    n=int(input("1.insert 2.traverse 3.delete 4.reverse : "))
    if n==1:
        obj.head=obj.insert(obj.head,int(input("enter the value :")))
    elif n==2:
        obj.traverse()
    elif n==3:
        obj.head=obj.delete(obj.head,int(input("enter the value to delete :")))
    elif n==4:
        obj.reverse()