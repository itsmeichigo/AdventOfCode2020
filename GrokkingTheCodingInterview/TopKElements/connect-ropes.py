# Given ‘N’ ropes with different lengths, we need to connect these ropes 
# into one big rope with minimum cost. The cost of connecting two ropes is 
# equal to the sum of their lengths.

# Example:
# Input: [1, 3, 11, 5]
# Output: 33
# Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). 
# So the total cost is 33 (4+9+20)

from heapq import heappush, heappop, heapify

def minimum_cost_to_connect_ropes(ropeLengths):
    result = 0
    min_heap = list(ropeLengths) # N space
    heapify(min_heap) # Nlog(N) times
    while len(min_heap) > 1: # N times
        cost = heappop(min_heap) + heappop(min_heap)
        result += cost
        heappush(min_heap, cost)
    return result


def main():
    print("Minimum cost to connect ropes: " +
            str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
            str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
            str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))

main()