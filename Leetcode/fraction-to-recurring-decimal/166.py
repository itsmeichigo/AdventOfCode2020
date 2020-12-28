def print_decimal(numerator, denominator):
    if denominator == 0:
        return None
    result = str(numerator / denominator)
    value, fraction = result.split(".")
    if int(fraction) == 0: result = value
    else:
        digit_map = {}
        for char in fraction:
            if char not in digit_map: digit_map[char] = 1
            else: digit_map[char] += 1
        if len(digit_map) == 1:
            key = list(digit_map.keys())[0]
            if digit_map[key] > 1:
                result = value + "." + "(" + key + ")"
        else:
            result = value + "." + "(" + fraction[:len(digit_map)] + ")"
    return result

assert(print_decimal(1, 0)) is None
assert(print_decimal(1, 2)) == "0.5"
assert(print_decimal(2, 1)) == "2"
assert(print_decimal(2, 3)) == "0.(6)"
assert(print_decimal(88, 77)) == "1.(142857)"