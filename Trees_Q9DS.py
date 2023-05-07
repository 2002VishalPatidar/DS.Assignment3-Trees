
class Node:
	def __init__(self, key):
		self.val = key
		self.left = self.right = None
def newNode(data):

	node = Node(0)
	node.data = data
	node.left = node.right = None
	return (node)

def maxLevel( root):

	if (root == None):
		return 0
	return (1 + max(maxLevel(root.left),
					maxLevel(root.right)))

sum = []

def maxLevelSum_( root, max_level , current):

	global sum
	
	if (root == None):
		return

	sum[current] += root.data

	maxLevelSum_(root.left, max_level,
				current + 1)
	maxLevelSum_(root.right, max_level,
				current + 1)

def maxLevelSum( root):

	global sum
	
	max_level = maxLevel(root)

	i = 0
	sum = [None] * (max_level + 2)
	while(i <= max_level + 1):
		sum[i] = 0
		i = i + 1

	maxLevelSum_(root, max_level, 1)

	maxSum = 0

	i = 1
	while ( i <= max_level ):
		maxSum = max(maxSum, sum[i])
		i = i + 1
	return maxSum


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.right = newNode(8)
root.right.right.left = newNode(6)
root.right.right.right = newNode(7)
print( maxLevelSum(root))
