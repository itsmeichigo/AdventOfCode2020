# Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.

# Example:
# Input: points = [[1,2],[1,3]], K = 1
# Output: [[1,2]]
# Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
# The Euclidean distance between (1, 3) and the origin is sqrt(10).
# Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

from heapq import heappop, heappush
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = sqrt((pow(x, 2) + pow(y, 2)))
    
    def __lt__(self, other):
        return self.distance > other.distance

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def find_closest_points(points, k):
    max_heap = []
    for i in range(0, len(points)):
        if i < k:
            heappush(max_heap, points[i])
        elif points[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, points[i])
    return max_heap


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()
main()