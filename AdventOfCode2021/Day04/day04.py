from typing import List, Tuple
from itertools import chain

def parse_input(file_name) -> Tuple[List[int], List[List[List[int]]]]:
    with open(file_name) as file:
        parsed_data = file.read().split("\n\n")
        numbers = [int(i) for i in parsed_data[0].split(",")]
        boards = [lines.splitlines() for lines in parsed_data[1:]]
        sanatized_boards = []
        for board in boards:
            lines = []
            for line in board:
                content = line.strip()
                lines.append([int(i) for i in content.split()])
            sanatized_boards.append(lines)
        return numbers, sanatized_boards

def play_bingo(numbers, boards, find_first_board=True) -> int:
    number_of_lines = len(boards[0])
    number_of_numbers_per_line = len(boards[0][0])
    board_rows = [[[] for i in range(number_of_lines)] for board in boards]
    board_columns = [[[] for i in range(number_of_numbers_per_line)] for board in boards]
    unmarked_numbers = [list(chain(*board)) for board in boards]
    complete_count = [0 for board in boards]
    for number in numbers:
        for i in range(len(boards)):
            board = boards[i]
            for line_index in range(number_of_lines):
                line = board[line_index]
                if number in line:
                    column_index = line.index(number)
                    board_rows[i][line_index].append(number)
                    board_columns[i][column_index].append(number)
                    if number in unmarked_numbers[i]:
                        index = unmarked_numbers[i].index(number)
                        unmarked_numbers[i].pop(index)
                    if len(board_rows[i][line_index]) == number_of_numbers_per_line or len(board_columns[i][column_index]) == number_of_lines:
                        current_result = sum(unmarked_numbers[i]) * number
                        if find_first_board:
                            return current_result
                        else:
                            complete_count[i] += 1
                            if 0 not in complete_count:
                                return current_result
    return 0

test_numbers, test_boards = parse_input("test.txt")
assert play_bingo(test_numbers, test_boards) == 4512
assert play_bingo(test_numbers, test_boards, find_first_board=False) == 1924

numbers, boards = parse_input("data.txt")
print("Part 1: ", play_bingo(numbers, boards))
print("Part 2: ", play_bingo(numbers, boards, find_first_board=False))
