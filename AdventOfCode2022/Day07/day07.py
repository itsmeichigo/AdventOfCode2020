from collections import deque
from re import search

class Directory:
    def __init__(self, name, children, files, parent):
        self.name = name
        self.children = children
        self.files = files
        self.parent = parent

    def calculate_size(self):
        return sum(self.files) + sum(c.calculate_size() for c in self.children)

def parse_dirs(lines):
    dirs_queue = deque()
    dirs = []
    current_dir = None
    for line in lines:
        dir_match = search("(?<=\$\scd\s)(\w+|\/)", line)
        file_size_match = search("\d+", line)
        sub_dir_match = search("(?<=dir\s)\w+", line)
        if dir_match is not None:
            name = dir_match.group()
            parent = None if len(dirs_queue) == 0 else dirs_queue[-1]
            current_dir = Directory(name, [], [], parent)
            if parent is not None:
                parent.children.append(current_dir)
            dirs_queue.append(current_dir)
            dirs.append(current_dir)
        elif search("(?<=\$\scd\s)..", line) is not None:
            dirs_queue.pop()
            current_dir = dirs_queue[-1]
        elif file_size_match is not None:
            file_size = int(file_size_match.group())
            current_dir.files.append(file_size)
    return dirs

with open("input.txt") as file:
    lines = file.read().splitlines()
    dirs = parse_dirs(lines)
    sizes = [d.calculate_size() for d in dirs]
    total_size_dir_lower_than_100K = sum(s for s in sizes if s <= 100_000)
    print(total_size_dir_lower_than_100K)

    root_size = sizes[0]
    unused_space = 70_000_000 - root_size
    minimum_needed_space = 30_000_000 - unused_space
    sizes.sort()
    index, found = 0, 0
    for size in sizes:
        if size >= minimum_needed_space:
            found = size
            break
    print(found)