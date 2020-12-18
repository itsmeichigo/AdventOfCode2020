import operator

ops = {
    "+" : operator.add,
    "*" : operator.mul,
}

def calculate(expression, advanced):
    while True:
        try:
            found = expression.index("(")
            expression = replace_bracket_content(expression, found, advanced)
        except:
            break

    if advanced:
        while True:
            try:
                found = expression.index("+")
                expression = replace_sum(expression, found)
            except:
                break
    
    index, left, result = 0, 0, 0
    op = None
    while index < len(expression):
        char = expression[index]
        if char.isdigit() and op is None:
            left = int(char)
            result = left
        elif char.isdigit(): 
            left = op(left, int(char))
            result = left
        elif char in ops.keys(): op = ops.get(char)
        index += 1
    return result

def replace_bracket_content(expression, index, advanced):
    open_brace = 1
    close_index = index + 1
    # find matching close and find result for content
    while close_index < len(expression):
        if expression[close_index] == ")": open_brace -= 1
        elif expression[close_index] == "(": open_brace += 1
        if open_brace == 0: 
            break
        else: close_index += 1
    content = calculate(expression[(index + 1):close_index], advanced)
    return expression[:index] + [str(content)] + expression[(close_index + 1):]

def replace_sum(expression, index):
    left, right = index - 1, index + 1
    result = int(expression[left]) + int(expression[right])
    return expression[:left] + [str(result)] + expression[(right + 1):]

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
        assert(calculate(list(k.replace(" ", "")), False)) == v

    test2 = {
        "1 + 2 * 3 + 4 * 5 + 6": 231,
        "1 + (2 * 3) + (4 * (5 + 6))": 51,
        "2 * 3 + (4 * 5)": 46,
        "5 + (8 * 3 + 9 + 3 * 4 * 3)": 1445,
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 669060,
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": 23340
    }
    for k, v in test2.items():
        items = list(k.replace(" ", ""))
        assert(calculate(items, True)) == v

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        items = [list(l.replace(" ", "")) for l in file.read().splitlines()]
        print(sum(calculate(i, False) for i in items))
        print(sum(calculate(i, True) for i in items))