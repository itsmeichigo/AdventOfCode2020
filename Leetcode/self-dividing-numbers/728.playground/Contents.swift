/*
 * 728. Self Dividing Numbers
 * https://leetcode.com/problems/self-dividing-numbers/
 */

import Foundation

func selfDividingNumbers(from min: Int, to max: Int) -> [Int] {
    var results: [Int] = []
    
    for i in min...max {
        
        let dividableNumbers = String(i)
            .map { String($0) }
            .map { Int($0) ?? 0 }
            .reduce([]) { (acc, current) -> [Int] in
                if current != 0 && i%current == 0 {
                    return acc + [current]
                }
                return acc
            }
        
        if dividableNumbers.count == String(i).count {
            results.append(i)
        }
    }
    
    return results
}

selfDividingNumbers(from: 66, to: 708)
