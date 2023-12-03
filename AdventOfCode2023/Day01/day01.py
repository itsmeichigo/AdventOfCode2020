def simple_cal(lines): 
    numbers = []
    for line in lines:
        digits = [s for s in line if s.isdigit()]
        numbers.append(int(digits[0] + digits[-1]))
    return numbers

def advanced_cal(lines):
    numbers = []
    number_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for line in lines:
        first, second = "", ""
        for i, line in enumerate(line):
            if line.isdigit():
                first = line
                break
            else:
                substring = line[:i+1]
                for key, value in number_map.items():
                    if key in substring:
                        first = value
                        break
                if first != "":
                    break
        for j in reversed(range(len(line))):
            if line[j].isdigit():
                second = line[j]
                break
            else:
                substring = line[j-1:]
                for key, value in number_map.items():
                    if key in substring:
                        second = value
                        break
                if second != "":
                    break
        numbers.append(int(first + second))
    return numbers

with open("data.txt", encoding='UTF-8') as file:
    lines = file.read().splitlines()
    print(sum(simple_cal(lines)))
    print(sum(advanced_cal(lines)))