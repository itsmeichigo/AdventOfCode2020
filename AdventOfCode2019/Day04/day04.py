def password_count(input, p2):
    r_min, r_max = [int(i) for i in input.split("-")]
    return sum(1 for i in range(r_min, r_max+1) if check_valid(str(i), p2))
    
def check_valid(password, p2):
    if not all(password[i] <= password[i+1] for i in range(len(password)-1)):
        return False
    counts = [password.count(c) for c in set(password)]
    if p2:
        return any(count == 2 for count in counts)
    else:
        return any(count >= 2 for count in counts)
    
assert(check_valid("111111", False)) == True
assert(check_valid("223450", False)) == False
assert(check_valid("123789", False)) == False
assert(check_valid("444444", True)) == False

input = "402328-864247"
print(password_count(input, False))
print(password_count(input, True))