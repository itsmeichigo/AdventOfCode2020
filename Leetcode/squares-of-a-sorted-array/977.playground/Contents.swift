/*
 * 977. Squares of a sorted array
 * https://leetcode.com/problems/squares-of-a-sorted-array
 */

import Foundation

/// easier, slower
func sortedSquares(input: [Int]) -> [Int] {
    return input.map { $0 * $0 }.sorted()
}

/// Time complexity: O(N) 🤯
/// #TIL: if array is already sorted, it can be used to write a cool algorithm (better time complexity than sorting again)
func alternativeResultSquares(input: [Int]) -> [Int] {
    var i = 0
    for (index, number) in input.enumerated() {
        if number > 0 {
            i = index
            break
        }
    }
    
    var j = i - 1
    
    var result: [Int] = []
    
    while j >= 0, i < input.count {
        if input[i] * input[i] < input[j] * input[j] {
            result.append(input[i] * input[i])
            i += 1
        } else {
            result.append(input[j] * input[j])
            j -= 1
        }
    }
    
    while i < input.count {
        result.append(input[i] * input[i])
        i += 1
    }
    
    while j > 0 {
        result.append(input[j] * input[j])
        j -= 1
    }
    
    return result
}

sortedSquares(input: [-4, -1, 0, 3, 10])
alternativeResultSquares(input: [-4, -1, 0, 3, 10])
