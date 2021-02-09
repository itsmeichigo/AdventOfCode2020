# Design a class that simulates a Stack data structure, implementing the following 
# two operations:

# push(int num): Pushes the number ‘num’ on the stack.
# pop(): Returns the most frequent number in the stack. If there is a tie, return 
# the number which was pushed later.

# Example:
# After following push operations: push(1), push(2), push(3), push(2), push(1), 
# push(2), push(5):
# 1. pop() should return 2, as it is the most frequent number
# 2. Next pop() should return 1
# 3. Next pop() should return 2

from heapq import heappush, heappop

class Item:
    def __init__(self, num, frequency, index):
        self.frequency = frequency
        self.index = index
        self.num = num

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.index > other.index
        return self.frequency > other.frequency

class FrequencyStack:
    index = 0
    max_heap = []
    frequency_map = {}

    def push(self, num):
        frequency = self.frequency_map.get(num, 0) + 1
        new_item = Item(num, frequency, self.index)
        self.index += 1
        heappush(self.max_heap, new_item)
        self.frequency_map[num] = frequency

    def pop(self):
        item = heappop(self.max_heap)
        new_frequency = item.frequency - 1
        if new_frequency == 0:
            del self.frequency_map[item.num]
        else:
            self.frequency_map[item.num] = new_frequency

        return item.num

def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())

main()