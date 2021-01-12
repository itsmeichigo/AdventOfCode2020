# Given a binary tree, find the length of its diameter. The diameter of a tree 
# is the number of nodes on the longest path between any two leaf nodes. 
# The diameter of a tree may or may not pass through the root.
# Note: You can always assume that there are at least two leaf nodes in the 
# given tree.
from treenode import TreeNode

class TreeDiameter:
    def __init__(self):
        self.tree_diameter = 0
    
    def find_diameter(self, root):
        self.check_diameter(root)
        return self.tree_diameter

    def check_diameter(self, current_node):
        if current_node is None:
            return 0
        left_diameter = self.check_diameter(current_node.left)
        right_diameter = self.check_diameter(current_node.right)
        current_diameter = left_diameter + right_diameter + 1
        self.tree_diameter = max(current_diameter, self.tree_diameter)
        return max(left_diameter, right_diameter) + 1

def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()