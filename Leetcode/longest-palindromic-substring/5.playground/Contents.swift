import Foundation

extension String {
    var isPalindromic: Bool {
        let charList = Array(self)
        for i in 0..<count/2 {
            if charList[i] == charList[count - i - 1] {
                continue
            } else {
                return false
            }
        }
        
        return true
    }
    
    func findPalindrome(left: Int, right: Int, maxLength: inout Int, start: inout Int) {
        let charList = Array(self)
        var l = left
        var r = right
        
        while l>=0, r<count, charList[l] == charList[r] {
            l -= 1
            r += 1
        }
        
        if maxLength < r - l - 1 {
            maxLength = r - l - 1
            start = l + 1
        }
    }
}

// bruteforce, terrible
func longestPalindromicSubstring(in string: String) -> String {
    if string.isPalindromic || string.count == 1 { return string }
    for i in (2...string.count-1).reversed() {
        for j in 0...string.count-i {
            let suffix = string.suffix(string.count-j)
            let substring = String(suffix.prefix(i))
            if substring.isPalindromic {
                return substring
            }
        }
    }
    return String(string.prefix(1))
}

func betterLongestPalindrome(in string: String) -> String {
    if string.count == 1 { return string }
    
    var maxLength = 0
    var start = 0
    
    for i in 0..<string.count {
        string.findPalindrome(left: i, right: i, maxLength: &maxLength, start: &start)
        string.findPalindrome(left: i, right: i+1, maxLength: &maxLength, start: &start)
    }
    
    return String(String(string.suffix(string.count - start)).prefix(maxLength))
}

extension String {
    static func randomString(ofLength length: Int) -> String {
        let characters = Array("qwertyuiopasdfghjklzxcvbnm")
        var string = ""
        for _ in 0..<1000 {
            string += String(characters.randomElement()!)
        }
        
        return string
    }
}

let string = String.randomString(ofLength: 1000)
//longestPalindromicSubstring(in: string)
betterLongestPalindrome(in: string)


