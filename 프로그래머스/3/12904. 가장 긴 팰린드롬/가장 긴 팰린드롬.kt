class Solution {
    fun solution(s: String): Int {
        for (offset in s.length downTo 1) {
            for (j in 0..s.length - offset) {
                var isPalindrome = true
                var startIdx = j
                var endIdx = j+offset-1
                for (k in 0 until (offset / 2)) {
                    if (s[startIdx+k] != s[endIdx-k]) {
                        isPalindrome = false
                        break
                    }
                }
                if (isPalindrome) {
                    return offset
                }
            }
        }
        return Int.MIN_VALUE
    }
}