import UIKit

var str = "Hello, playground"

// Time: O(N)
// Space: 1
func getWarmerDayCountList(for temperatures: [Int]) -> [Int] {
    var countList: [Int] = []
    
    for i in 0..<temperatures.count - 1 {
        for j in i+1..<temperatures.count {
            if temperatures[j] > temperatures[i] {
                countList.append(j - i)
                break
            }
        }
        
        if countList.count < i + 1 {
            countList.append(0)
        }
    }
    
    countList.append(0)
    return countList
}

let temp = [73, 74, 75, 71, 69, 72, 76, 73]
getWarmerDayCountList(for: temp)
