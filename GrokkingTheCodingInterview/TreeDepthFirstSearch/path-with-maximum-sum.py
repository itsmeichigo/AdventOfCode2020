# Find the path with the maximum sum in a given binary tree. 
# Write a function that returns the maximum sum.
# A path can be defined as a sequence of nodes between any two nodes 
# and doesn’t necessarily pass through the root. The path must contain 
# at least one node.
from treenode import TreeNode
from math import inf

class PathSum:
    def find_maximum_path_sum(self, root):
        self.max_path_sum = -inf
        self.calculate_path_sum(root)
        return self.max_path_sum

    def calculate_path_sum(self, current_node):
        if current_node is None:
            return 0
        left_path_sum = max(self.calculate_path_sum(current_node.left), 0)
        right_path_sum = max(self.calculate_path_sum(current_node.right), 0)
        current_path_sum = left_path_sum + right_path_sum + current_node.val
        self.max_path_sum = max(current_path_sum, self.max_path_sum)
        return max(left_path_sum, right_path_sum) + current_node.val

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    pathSum = PathSum()
    print("Maximum Path Sum: " + str(pathSum.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(pathSum.find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(pathSum.find_maximum_path_sum(root)))

main()