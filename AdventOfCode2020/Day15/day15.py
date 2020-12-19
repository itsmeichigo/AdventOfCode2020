def find_number(starting, end):
    acc = [int(i) for i in starting.split(",")]
    num_map = dict(zip(acc, [i for i in range(len(starting))]))
    acc.append(0) # assuming starting list contains only distinct numbers
    for i in range(len(acc), end):
        last_num = acc[i-1]
        if last_num not in num_map: 
            acc.append(0)
        else:
            result = i - 1 - num_map[last_num]
            acc.append(result)
        num_map[last_num] = i - 1
    return acc[-1]

def test_input():
    assert(find_number("0,3,6", 2020)) == 436
    assert(find_number("1,3,2", 2020)) == 1
    assert(find_number("2,1,3", 2020)) == 10
    assert(find_number("1,2,3", 2020)) == 27
    assert(find_number("2,3,1", 2020)) == 78
    assert(find_number("3,2,1", 2020)) == 438
    assert(find_number("3,1,2", 2020)) == 1836

if __name__ == "__main__":
    test_input()
    print(find_number("1,0,18,10,19,6", 2020))
    print(find_number("1,0,18,10,19,6", 30000000))