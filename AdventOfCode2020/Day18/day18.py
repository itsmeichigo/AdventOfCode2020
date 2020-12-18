import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

def calculate(expression):
    result, left, op = 0, 0, None
    index = 0
    while index < len(expression):
        char = expression[index]
        if char == "(":
            open_brace = 1
            close_index = index + 1
            # find matching close and find result for content
            while close_index < len(expression):
                if expression[close_index] == ")": open_brace -= 1
                elif expression[close_index] == "(": open_brace += 1
                if open_brace == 0: break
                else: close_index += 1
            content = calculate(expression[(index + 1):close_index])
            if op is None: left = content
            else:
                left = op(left, content)
                result = left
            index = close_index + 1
        else:
            if char.isdigit() and op is None: left = int(char)
            elif char.isdigit(): 
                left = op(left, int(char))
                result = left
            elif char in ops.keys(): op = ops.get(char)
            index += 1
            
    return result

def test_input():
    test1 = {
        "1 + 2 * 3 + 4 * 5 + 6": 71,
        "1 + (2 * 3) + (4 * (5 + 6))": 51,
        "2 * 3 + (4 * 5)": 26,
        "5 + (8 * 3 + 9 + 3 * 4 * 3)": 437,
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 12240,
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": 13632
    }

    for k, v in test1.items():
        assert(calculate(k)) == v
    
if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        print(sum(calculate(e) for e in file.read().splitlines()))