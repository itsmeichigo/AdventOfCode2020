# Given two integer arrays to represent weights and profits of ‘N’ items, 
# we need to find a subset of these items which will give us maximum profit 
# such that their cumulative weight is not more than a given number ‘C.’ 
# Each item can only be selected once, which means either we put an item in 
# the knapsack or we skip it.

def solve_knapsack_top_down(profits, weights, capacity):
    cache = [[-1 for x in range(capacity + 1)] for y in range(len(weights))] # O(N*C) space
    return recursive_top_down(profits, weights, capacity, cache, 0) # O(N*C) times

def recursive_top_down(profits, weights, capacity, cache, current_index):
    if capacity == 0 or current_index >= len(weights):
        return 0

    if cache[current_index][capacity] != -1:
        return cache[current_index][capacity]

    profit1 = 0
    if capacity - weights[current_index] >= 0:
        profit1 = profits[current_index] + recursive_top_down(profits, weights, capacity - weights[current_index], cache, current_index + 1)

    profit2 = recursive_top_down(profits, weights, capacity, cache, current_index + 1)
    profit = max(profit1, profit2)
    cache[current_index][capacity] = profit
    return profit

def solve_knapsack_bottom_up(profits, weights, capacity):
    n = len(profits)
    if capacity == 0 or n == 0 or n != len(weights):
        return 0

    dp = [[0 for x in range(capacity + 1)] for y in range(n)] # O(N*C) space

    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # O(N*C) times
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)
    
    return dp[n-1][capacity]

def solve_knapsack_bottom_up_optimized(profits, weights, capacity):
    n = len(weights)
    if capacity == 0 or n == 0 or n != len(profits): return 0
    dp = [0 for x in range(capacity+1)] # O(C) space

    for c in range(capacity+1):
        if weights[0] <= c:
            dp[c] = weights[0]

    # O(N*C) times
    for i in range(n):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[c - weights[i]]
            profit2 = dp[c]
            dp[c] = max(profit1, profit2)

    return dp[capacity]

def main():
    print(solve_knapsack_bottom_up_optimized([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack_bottom_up_optimized([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_bottom_up_optimized([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()