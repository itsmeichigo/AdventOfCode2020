# Find the minimum depth of a binary tree. The minimum depth 
# is the number of nodes along the shortest path from the 
# root node to the nearest leaf node.

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def find_minimum_depth(root):
    minimum_depth = 0
    if root is None: return minimum_depth
    nodes = deque([root])
    while nodes:
        minimum_depth += 1
        for _ in range(len(nodes)):
            current = nodes.popleft()
            if current.left is None and current.right is None:
                return minimum_depth
            if current.left: nodes.append(current.left)
            if current.right: nodes.append(current.right)
    return minimum_depth

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
main()