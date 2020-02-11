class cnode:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None

while True:
    print("*************** main menu *****************")
    choice=int(input("1.create 2.insert 3.view 4.search \n enter your choice : "))
    if choice==1:
        val=int(input("enter the value : "))
        root = cnode(val)
        head=root
    if choice==2:
        def insert(node,value):
            if node.value:
                if value<node.value:
                    if node.left:
                        return insert(node.left,value)
                    else:
                        node.left=cnode(value)
                        print("value inserted at left")
                        return True
                else:
                    if node.right:
                        return insert(node.right,value)
                    else:
                        node.right=cnode(value)
                        print("value inserted at right")
                        return True
            else:
                node.value=value
                print("value inserted at root")
                return True
        value=int(input("enter the value : "))
        insert(root,value)

    if choice==3:
        print(f"head value is : {head.value}  \nleft child value is : {head.left.value}  \nright child value is : {head.right.value}")

    if choice==4:
        def search(node,value):
            if node.value==value:
                print("value has been found : ",node.value)
                return True
            elif value<node.value:
                return search(node.left,value)
            elif value>=node.value:
                return search(node.right,value)
            else:
                print("value not found sorry :( ")
                return False
        value=int(input("enter the value to search : "))
        search(root,value)

    else:
        pass