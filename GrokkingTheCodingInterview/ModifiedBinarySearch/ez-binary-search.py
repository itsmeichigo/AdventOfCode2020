# Given a sorted array of numbers, find if a given number ‘key’ is present 
# in the array. Though we know that the array is sorted, we don’t know if 
# it’s sorted in ascending or descending order. You should assume that the 
# array can have duplicates.

# Write a function to return the index of the ‘key’ if it is present in the 
# array, otherwise return -1.

# O(logN)

def binary_search(arr, key):
  is_asc = arr[0] < arr[-1]
  index = len(arr) // 2
  while index >= 0 and index < len(arr):
    if arr[index] == key:
      return index
    
    if (arr[index] < key and is_asc) or (arr[index] > key and not is_asc):
      index += 1
    else:
      index -= 1
  return -1

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()