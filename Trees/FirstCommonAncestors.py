class Node:

    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

#Sort the arr first
def createMinBST(arr,start,end):

    if end < start:
        return None

    mid =(start+end)//2
    root = Node(arr[mid])
    root.left = createMinBST(arr,start,mid-1)
    root.right = createMinBST(arr,mid+1,end)

    return root

def print_ancestors(root,target):
    res=[]
    if root==None:
        return False

    if root.data == target:
            return True

    if (print_ancestors(root.left,target) or print_ancestors(root.right,target)):
        if root.data not in res:
            res.append(root.data)
            # print(root.data)
        return res


    return False

def LCA(root,node1,node2):
    if root == None:
        return None

    if root.data < node1 and root.data < node2:
        return LCA(root.right,node1,node2)

    if root.data > node1 and root.data >node2:
        return LCA(root.left,node1,node2)

    return root.data

List =[1,2,3,4,5,6]
#List from which BST will be created
root = createMinBST(List,0,len(List)-1)
print(LCA(root,1,2))
