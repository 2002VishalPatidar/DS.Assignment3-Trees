class newNode:
     
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLeafNodes(root):
     
    if root == None:
        return
    if (root.left == None and
        root.right == None):
        print(root.data, end = " ")
        return
     
    if root.right:
        printLeafNodes(root.right)
     
    if root.left:
        printLeafNodes(root.left)
 

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)

 
printLeafNodes(root)