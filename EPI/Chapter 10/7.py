#locking API
class Node:
    def __init__(self,key):
        self.l_child=None
        self.r_child=None
        self.data=key
        self.isLocked=False
        self.parent=None
class Tree:
    def __init__(self):
        self.root=None
        self.size=0

    def binary_insert(self,root,node):
        if root is None :
            root =node
        else:
            if root.data > node.data:
                if root.l_child is None:
                    root.l_child = node
                    node.parent = root
                else:
                    self.binary_insert(root.left,node)
            else:
                if root.r_child is None:
                    root.r_child = node
                    node.parent = root
                else:
                    self.binary_insert(root.right,node)

    def print_preorder(self,root):
        if not root:
            return
        print(root.data)
        self.print_preorder(root.l_child)
        self.print_preorder(root.r_child)

    def check_lock(self,root,node):
        if root is None:
            return False
        else:
            if root.data > node.data:
                return self.check_lock(root.l_child,node)
            elif root.data < node.data:
                return self.check_lock(root.r_child,node)
            else:
                # return "Node :",root.data," Locked :",root.isLocked
                return root.parent.isLocked

bst=Tree()
root = Node(3)
x=Node(1)
y=Node(4)
y.isLocked=True
bst.binary_insert(root,x)
bst.binary_insert(root,y)
print(bst.check_lock(root,Node(4)))
#Bst implemneted
