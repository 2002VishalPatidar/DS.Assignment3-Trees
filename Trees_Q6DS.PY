
class Node:
	def __init__(self, k):
		self.data = k
		self.left = None
		self.right = None
		
def sumAllLeftLeaf(node, isleft):
	
	if node is None:
		return 0
		
	if node.left is None and node.right is None and isleft:
		return node.data

	return sumAllLeftLeaf(node.left, True) + sumAllLeftLeaf(node.right, False)

root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.left.right = Node(12)
root.left.left = Node(5)
root.right.left = Node(23)
root.right.right = Node(52)
root.left.right.right = Node(12)
root.right.right.left = Node(50)

print("The sum of leaf is " + str(sumAllLeftLeaf(root, False)))

