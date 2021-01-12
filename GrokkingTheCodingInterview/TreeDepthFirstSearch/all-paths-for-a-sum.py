# Given a binary tree and a number ‘S’, find all paths from root-to-leaf 
# such that the sum of all the node values of each path equals ‘S’.
from treenode import TreeNode

def find_paths(root, targeted_sum):
    all_paths = []
    find_paths_recursive(root, targeted_sum, [], all_paths)
    return all_paths

def find_paths_recursive(current, targeted_sum, current_path, all_paths):
    if current is None: return
    current_path.append(current.val)
    if not current.left and not current.right and current.val == targeted_sum:
        all_paths.append(list(current_path)) # make a copy of current path before appending
    else:
        find_paths_recursive(current.left, targeted_sum - current.val, current_path, all_paths)
        find_paths_recursive(current.right, targeted_sum - current.val, current_path, all_paths)
    del current_path[-1]

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
            ": " + str(find_paths(root, sum)))


main()
