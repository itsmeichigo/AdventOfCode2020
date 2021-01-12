# Given a binary tree and a number ‘S’, find all paths in the tree 
# such that the sum of all the node values of each path equals ‘S’. 
# Please note that the paths can start or end at any node but all paths 
# must follow direction from parent to child (top to bottom).
from treenode import TreeNode

def count_paths(root, S):
    # return check_path(root, 0, S, [])
    return optimized_check_path(root, [], S)

def check_path(current_node, current_sum, target_sum, current_path):
    if current_node is None:
        return 0
    current_sum += current_node.val
    current_path.append(current_node.val)
    if current_sum > target_sum:
        current_sum -= current_path[0]
        current_path = current_path[1:]
    elif current_sum == target_sum:
        return 1
    return check_path(current_node.left, current_sum, target_sum, list(current_path)) + \
        check_path(current_node.right, current_sum, target_sum, list(current_path))

def optimized_check_path(current_node, current_path, target_sum):
    if current_node is None: 
        return 0
    current_path.append(current_node.val)
    current_sum, total_count = 0, 0
    for i in range(len(current_path)-1, -1, -1):
        current_sum += current_path[i]
        if current_sum == target_sum:
            total_count += 1
    total_count += optimized_check_path(current_node.left, current_path, target_sum)
    total_count += optimized_check_path(current_node.right, current_path, target_sum)
    del current_path[-1]
    return total_count

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))

main()