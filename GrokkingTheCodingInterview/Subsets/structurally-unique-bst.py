# Given a number ‘n’, write a function to return all structurally 
# unique Binary Search Trees (BST) that can store values 1 to ‘n’?

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_unique_trees(n):
    if n <= 0: return []    
    return find_recursive(1, n)

def find_recursive(start, end):
    result = []
    if start > end:
        result.append(None)
        return result
    for i in range(start, end+1):
        left_nodes = find_recursive(start, i-1)
        right_nodes = find_recursive(i+1, end)
        for left in left_nodes:
            for right in right_nodes:
                node = TreeNode(i)
                node.left = left
                node.right = right
                result.append(node) 
    return result

def count_trees(n):
    return count_trees_recursive({}, n)

def count_trees_recursive(cache, n):
    if n in cache: return cache[n]
    if n <= 1: return 1
    count = 0
    for i in range(1, n+1):
        count_left = count_trees(i-1)
        count_right = count_trees(n-i)
        count += (count_left * count_right)
    cache[n] = count
    return count

def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))
    
    print("Count trees: " + str(count_trees(2)))
    print("Count trees: " + str(count_trees(3)))


main()