# Given a binary tree and a number sequence, find if the sequence is 
# present as a root-to-leaf path in the given tree.
from treenode import TreeNode

def find_path(root, sequence):
    return check_recursive(root, sequence)

def check_recursive(current_node, sequence):
    if current_node is None:
        return len(sequence) == 0
    if len(sequence) > 0 and current_node.val == sequence[0]:
        return check_recursive(current_node.left, sequence[1:]) or \
            check_recursive(current_node.right, sequence[1:])
    return False

def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()