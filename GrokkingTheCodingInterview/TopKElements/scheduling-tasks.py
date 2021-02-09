# You are given a list of tasks that need to be run, in any order, on a server. 
# Each task will take one CPU interval to execute but once a task has finished, 
# it has a cooling period during which it can’t be run again. If the cooling 
# period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals 
# that the server needs to finish all tasks.

# If at any time the server can’t execute any task then it must stay idle.

# Example:
# Input: [a, a, a, b, c, c], K=2
# Output: 7
# Explanation: a -> c -> b -> a -> c -> idle -> a

from heapq import heappush, heappop
from collections import deque

def schedule_tasks(tasks, k):
    intervalCount = 0
    frequency_map = {}
    for task in tasks:
        frequency_map[task] = frequency_map.get(task, 0) + 1

    max_heap = []
    for task, frequency in frequency_map.items():
        heappush(max_heap, (-frequency, task))

    queue = deque()
    while max_heap:
        frequency, task = heappop(max_heap)
        intervalCount += 1
        queue.append((task, frequency + 1))
        if len(queue) > k:
            task, frequency = queue.popleft()
            if -frequency > 0:
                heappush(max_heap, (frequency, task))
    
    while queue:
        task, frequency = queue.popleft()
        if frequency == 0: 
            continue
        intervalCount += (k - len(queue) + 1)
        queue.append((task, frequency + 1))

    return intervalCount


def main():
    print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()