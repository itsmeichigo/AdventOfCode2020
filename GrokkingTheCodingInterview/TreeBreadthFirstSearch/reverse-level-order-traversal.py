# Given a binary tree, populate an array to represent its 
# level-by-level traversal in reverse order, i.e., the lowest 
# level comes first. You should populate the values of all nodes 
# in each level from left to right in separate sub-arrays.

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = deque()
    nodes = deque([root])
    while nodes:
        level_size = len(nodes)
        level_values = []
        for _ in range(level_size):
            current = nodes.popleft()
            level_values.append(current.val)
            if current.left: nodes.append(current.left)
            if current.right: nodes.append(current.right)
        result.appendleft(level_values)
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: ", str(traverse(root)))

main()