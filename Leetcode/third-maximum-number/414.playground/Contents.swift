import Foundation

// suppose array contains only positive integers
func thirdMaximumNumber(in array: [Int]) -> Int {
    var max = -1
    var secondMax = -1
    var thirdMax = -1
    
    for number in array {
        if number == max || number == secondMax || number == thirdMax {
            continue
        }
        
        if number > max {
            thirdMax = secondMax
            secondMax = max
            max = number
        } else if number > secondMax {
            thirdMax = secondMax
            secondMax = number
        } else if number > thirdMax {
            thirdMax = number
        }
    }
    
    if thirdMax == -1 { return max }
    return thirdMax
}

thirdMaximumNumber(in: [3, 2, 1])
thirdMaximumNumber(in: [1, 2])
thirdMaximumNumber(in: [2, 2, 3, 1])
