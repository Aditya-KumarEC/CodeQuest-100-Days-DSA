class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def binarytree(values):
    if not values:
        return None
    New_Nodes=[node(val) for val in values]
    root=New_Nodes[0]
    i=0 #parent index
    j=1 #child index
    while j<len(values):
        if i<len(New_Nodes):
            if j<len(New_Nodes):
                New_Nodes[i].left=New_Nodes[j]
                j+=1
            if j<len(New_Nodes):
                New_Nodes[i].right=New_Nodes[j]
                j+=1
        i+=1
    return root
def inorder_traversal(Node):
    if Node:       
        inorder_traversal(Node.left)
        print(Node.value,end=" ")     
        inorder_traversal(Node.right)
lis=list(map(int,input("Enter values:").split()))
root=binarytree(lis)
print("Inorder Traversal:")
inorder_traversal(root)

