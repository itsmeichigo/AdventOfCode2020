# Given a binary tree where each node can only have a digit (0-9) value, 
# each root-to-leaf path will represent a number. Find the total sum of all 
# the numbers represented by all paths.
from treenode import TreeNode

def find_sum_of_path_numbers(root):
    return traverse_path_recursive(root, 0)

def traverse_path_recursive(current_node, current_sum):
    if current_node is None: 
        return 0
    current_sum = current_sum * 10 + current_node.val
    if not current_node.left and not current_node.right:
        return current_sum
    return traverse_path_recursive(current_node.left, current_sum) + traverse_path_recursive(current_node.right, current_sum)

def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()