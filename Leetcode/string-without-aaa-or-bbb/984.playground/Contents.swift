/**
 * 984. String without AAA or BBB
 * https://leetcode.com/problems/string-without-aaa-or-bbb
 */

import UIKit

func resultString(a: Int, b: Int) -> String {
    var result = ""
    var isCurrentA = a >= b
    var remainingA = a
    var remainingB = b
    
    let resultLength = a + b
    while result.count < resultLength {
        let currentChar = isCurrentA ? "a" : "b"
        var repeatLength: Int
        if isCurrentA {
            repeatLength = remainingB == 0 ? remainingA : remainingA / remainingB >= 2 ? 2 : 1
            remainingA = max(0, remainingA - repeatLength)
        } else {
            repeatLength = remainingA == 0 ? remainingB : remainingB / remainingA >= 2 ? 2 : 1
            remainingB = max(0, remainingB - repeatLength)
        }
        result += String(repeating: currentChar, count: repeatLength)
        isCurrentA = !isCurrentA
    }
    
    return result
}

/// from official solution - neater but doesn't actually take `a` and `b` into account
func alternativeResultString(a: Int, b: Int) -> String {
    var result = ""
    var remainingA = a
    var remainingB = b
    
    while remainingA > 0 || remainingB > 0 {
        var isCurrentA: Bool
        if result.count >= 2 &&
            Array(result)[result.count - 1] == Array(result)[result.count-2] {
            isCurrentA = Array(result)[result.count - 1] == "b"
        } else {
            isCurrentA = a > b
        }
        
        if isCurrentA {
            remainingA -= 1
            result += "a"
        } else {
            remainingB -= 1
            result += "b"
        }
    }
    
    return result
}

resultString(a: 1, b: 4)
alternativeResultString(a: 1, b: 4)
