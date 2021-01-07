# Given a binary tree and a number ‘S’, find if the tree 
# has a path from root-to-leaf such that the sum of all 
# the node values of that path equals ‘S’.

from treenode import TreeNode

def has_path(root, sum):
    if not root: return False
    if not root.left and not root.right and root.val == sum:
        return True
    sum -= root.val 
    return has_path(root.left, sum) or has_path(root.right, sum)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))

main()