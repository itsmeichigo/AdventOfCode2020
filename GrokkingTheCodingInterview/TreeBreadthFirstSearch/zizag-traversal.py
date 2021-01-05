# Given a binary tree, populate an array to represent its 
# zigzag level order traversal. You should populate the 
# values of all nodes of the first level from left to right, 
# then right to left for the next level and keep alternating 
# in the same manner for the following levels.

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []
    if root is None: return result
    nodes = deque([root])
    left_first = True
    while nodes:
        level_size = len(nodes)
        level_values = deque()
        for _ in range(level_size):
            current = nodes.popleft()
            if left_first:
                level_values.append(current.val)
            else:
                level_values.appendleft(current.val)
            if current.left: 
                nodes.append(current.left)
            if current.right: 
                nodes.append(current.right)
        result.append(list(level_values))
        left_first = not left_first
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: ", str(traverse(root)))

main()