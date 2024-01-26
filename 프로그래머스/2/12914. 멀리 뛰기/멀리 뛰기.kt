class Solution {
    fun solution(n: Int): Long {
        
        val counts = LongArray(size = 2001)
        counts[1] = 1
        counts[2] = 2

        for (i in 3..2000) {
            counts[i] = (counts[i] + counts[i - 1] + counts[i - 2]) % 1234567
        }

        return counts[n]
    }
}