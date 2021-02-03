# For a given number ‘N’, write a function to generate all combination 
# of ‘N’ pairs of balanced parentheses.
# Example:
# Input: N=3
# Output: ((())), (()()), (())(), ()(()), ()()()
from collections import deque

class ParenthesesGroup:
    def __init__(self, content, open_count, close_count):
        self.content = content
        self.open_count = open_count
        self.close_count = close_count

def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesGroup("", 0, 0))
    while queue:
        current = queue.popleft()
        if current.open_count == num and current.close_count == num:
            result.append(current.content)
        else:
            if current.open_count < num:
                queue.append(ParenthesesGroup(
                    current.content + "(",
                    current.open_count + 1,
                    current.close_count
                ))
            if current.open_count > current.close_count:
                queue.append(ParenthesesGroup(
                    current.content + ")",
                    current.open_count,
                    current.close_count + 1
                ))
    return result

def generate_valid_parentheses_recursive(num):
    result = []
    combination = ["" for i in range(num*2)]
    recursive_call(num, combination, 0, 0, 0, result)
    return result

def recursive_call(num, combination, open_count, close_count, index, result):
    if open_count == num and close_count == num:
        result.append("".join(combination))
        return
    if open_count < num:
        updated = "".join(list(combination) + ["("])
        recursive_call(num, updated, open_count + 1, close_count, index + 1, result)
    if open_count > close_count:
        updated = "".join(list(combination) + [")"])
        recursive_call(num, updated, open_count, close_count + 1, index + 1, result)

def main():
    print("All combinations of balanced parentheses are: " +
            str(generate_valid_parentheses_recursive(2)))
    print("All combinations of balanced parentheses are: " +
            str(generate_valid_parentheses_recursive(3)))

main()