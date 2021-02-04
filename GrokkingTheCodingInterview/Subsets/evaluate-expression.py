# Given an expression containing digits and operations (+, -, *), 
# find all possible ways in which the expression can be evaluated 
# by grouping the numbers and operators using parentheses.

# Example:
# Input: "1+2*3"
# Output: 7, 9
# Explanation: 1+(2*3) => 7 and (1+2)*3 => 9

def diff_ways_to_evaluate_expression(input):
    return recursive_call({}, input)
            
def recursive_call(cache, input):
    if input in cache:
        return cache[input]
    result = []
    if "+" not in input and "-" not in input and "*" not in input:
        result.append(int(input))
    else:
        for i in range(len(input)):
            if not input[i].isdigit():
                left_side = diff_ways_to_evaluate_expression(input[:i])
                right_side = diff_ways_to_evaluate_expression(input[i+1:])
                for left_part in left_side:
                    for right_part in right_side:
                        new_str = str(left_part) + input[i] + str(right_part)
                        result.append(eval(new_str))
    cache[input] = result
    return result

def main():
    print("Expression evaluations: " +
            str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " +
            str(diff_ways_to_evaluate_expression("2*3-4-5")))

main()