#not completed
class Node:
    def __init__(self,val):
        self.val=val
        self.next =None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,val):
        temp = Node(val)
        if self.head ==None:
            self.head= temp
        else:
            temp.next=self.head
            self.head=temp

    def print_list(self):
        temp=self.head
        while temp!=None:
            print(temp.val)
            temp =temp.next

    def even_odd(self):
        even_head=odd_head=None
        t=1
        temp=self.head
        while temp!=None:
            Next = temp.next
            t^=1
            if t ==0:
                if even_head==None:
                    even_head =temp
                    even_head.next=None
                else:
                    t1=even_head
                    while t1!=None"
                    temp.next=None
                    even_head.next=temp
                #     even_head=temp
            else:
                if odd_head==None:
                    odd_head=temp
                # else:
                #     temp.next=odd_head
                #     even_head=temp

            temp=Next

        print(odd_head.val)
        print(even_head.val)



ll=LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
# ll.print_list()
ll.even_odd()
