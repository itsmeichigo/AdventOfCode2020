import Foundation

extension String {
    // Time: O(N/2), Space: O(1)
    func reverse() -> String {
        var charList = Array(self)
        for i in 0..<count/2 {
            let character = charList[i]
            charList[i] = charList[count - i - 1]
            charList[count - i - 1] = character
        }
        return String(charList)
    }
}

"hello".reverse()
