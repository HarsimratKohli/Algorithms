#Zipping of a linked list
class Node:

    def __init__(self,key):
        self.key=key
        self.next=None

class List:
    def __init__(self):
        self.head=None

    def add(self,key):
        tmp= Node(key)
        if self.head == None:
            self.head = tmp
        else:
            ptr=self.head
            while(ptr.next !=None):
                ptr=ptr.next
            ptr.next=tmp

    def disp(self):
        ptr= self.head
        while ptr != None:
            print(ptr.key)
            ptr=ptr.next

l=List()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
# l.disp()

def ReverseLinkedList(head):
    prev =None
    curr = head
    next = head

    while curr!=None:
        next =curr.next
        curr.next = prev
        prev= curr
        curr =next

    return prev

def Zipping_func(node):
    fast = slow = node
    while fast!=None and fast.next!=None:
        fast =fast.next.next
        slow = slow.next
    #slow gives the half of the List

    first_half_head = node
    second_half_head = slow.next

    slow.next = None

    second_half_head = ReverseLinkedList(second_half_head)

    first_half_ptr=first_half_head
    second_half_ptr=second_half_head
    while second_half_ptr!=None:
        tmp = second_half_ptr.next
        second_half_ptr.next = first_half_ptr.next
        first_half_ptr.next = second_half_ptr
        first_half_ptr = first_half_ptr.next.next
        second_half_ptr = tmp

    return first_half_head


node = l.head
# ReverseLinkedList(node)
ptr = Zipping_func(node)
while ptr:
    print(ptr.key)
    ptr=ptr.next
